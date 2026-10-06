# Sentiment Analysis API

REST API sederhana untuk klasifikasi sentimen teks berbahasa Indonesia (POSITIF / NEGATIF / NETRAL) menggunakan pendekatan **zero-shot prompting** dengan Google Gemini API, dibangun menggunakan FastAPI.

## Demo

- Local: `http://127.0.0.1:8000/docs`
- LIVE

## Fitur

- Klasifikasi sentimen teks bahasa Indonesia tanpa perlu training data (zero-shot)
- REST API dengan dokumentasi interaktif otomatis (Swagger UI)
- Validasi input otomatis menggunakan Pydantic
- Error handling untuk kegagalan request ke API eksternal

## Tech Stack

- **FastAPI** — web framework untuk membangun REST API
- **Pydantic** — validasi data request/response
- **Google Gemini API** (`gemini-3.5-flash-lite`) — model LLM untuk klasifikasi sentimen
- **Uvicorn** — ASGI server untuk menjalankan aplikasi

## Instalasi & Menjalankan Secara Lokal

### 1. Clone repository
```bash
git clone https://github.com/khoirulsr/sentiment-api.git
cd sentiment-api
```

### 2. Buat virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set API key
Dapatkan API key gratis dari [Google AI Studio](https://aistudio.google.com/apikey), lalu set sebagai environment variable:

```bash
# Windows PowerShell
$env:AI_STUDIO_API_KEY="AIzaSy..."

# macOS/Linux
export AI_STUDIO_API_KEY="AIzaSy..."
```

### 5. Jalankan server
```bash
uvicorn app:app --reload
```

### 6. Buka dokumentasi API
Buka browser ke `http://127.0.0.1:8000/docs`

## Contoh Penggunaan

**Request:**
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "Produknya bagus banget, pengiriman cepat!"}'
```

**Response:**
```json
{
  "text": "Produknya bagus banget, pengiriman cepat!",
  "sentiment": "POSITIF"
}
```

## Struktur Project

```
sentiment-api/
├── app.py              # Aplikasi FastAPI utama
├── requirements.txt    # Daftar dependency
├── .gitignore
└── README.md
```

## Evaluasi Model

Model diuji terhadap 70 data review berlabel (dataset PRDECT-ID), menghasilkan akurasi **95,6%** pada klasifikasi zero-shot tanpa fine-tuning tambahan.

## Catatan

Project ini dibuat sebagai bagian dari latihan portfolio AI Engineering, dengan fokus pada penerapan LLM untuk kasus sentiment analysis dan deployment sebagai REST API.

## Lisensi

MIT License
