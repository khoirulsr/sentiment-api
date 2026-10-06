from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
import os

# =====================================================================
# 1. SETUP
# =====================================================================
app = FastAPI(title="Sentiment Analysis API", version="1.0")

# API key diambil dari environment variable, BUKAN hardcode di kode.
# Cara set environment variable dijelaskan di langkah VS Code di bawah.
AI_STUDIO_API_KEY = os.environ.get("AI_STUDIO_API_KEY")

if not AI_STUDIO_API_KEY:
    raise ValueError(
        "AI_STUDIO_API_KEY tidak ditemukan! "
        "Set environment variable dulu sebelum menjalankan aplikasi."
    )

client = genai.Client(api_key=AI_STUDIO_API_KEY)


# =====================================================================
# 2. SKEMA DATA INPUT (request body)
# =====================================================================
class TextInput(BaseModel):
    text: str


class SentimentOutput(BaseModel):
    text: str
    sentiment: str


# =====================================================================
# 3. ENDPOINT
# =====================================================================
@app.get("/")
def home():
    """Endpoint untuk cek apakah API hidup."""
    return {"message": "Sentiment Analysis API aktif! Buka /docs untuk coba endpoint."}


@app.post("/predict", response_model=SentimentOutput)
def predict_sentiment(input: TextInput):
    """
    Menerima teks, mengembalikan hasil klasifikasi sentiment
    (POSITIF / NEGATIF / NETRAL) menggunakan zero-shot prompting ke Gemini.
    """
    prompt = f"""
    Klasifikasikan sentimen dari teks di bawah ini menjadi salah satu dari kategori berikut:
    - POSITIF
    - NEGATIF
    - NETRAL

    Aturan: Hanya berikan jawaban berupa 1 kata kategori tersebut (tanpa tanda titik,
    tanpa penjelasan tambahan).

    Teks: "{input.text}"
    Sentimen:
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
        )
        hasil_sentimen = response.text.strip()

        return SentimentOutput(text=input.text, sentiment=hasil_sentimen)

    except Exception as e:
        # Kalau ada error (misal limit API, server down, dll),
        # API akan kasih response error yang jelas, bukan crash diam-diam.
        raise HTTPException(status_code=500, detail=f"Gagal memproses: {str(e)}")
