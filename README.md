# Prediksi Cuaca Australia

Proyek ini dibuat untuk memprediksi apakah besok akan hujan di Australia atau tidak. Prosesnya dimulai dari analisis data di Jupyter Notebook, melatih model machine learning dengan XGBoost, hingga menjadi sebuah aplikasi web sederhana yang bisa dicoba.

Di dalam aplikasi web tersebut, Anda bisa mengunggah file data cuaca (dalam format CSV atau Excel), dan aplikasi akan memberikan prediksinya secara langsung.

## Apa Saja yang Ada di Proyek Ini?

- **Notebook Analisis**: File `Model Weather Prediction.ipynb` berisi semua langkah analisis data, mulai dari pembersihan, visualisasi, sampai pembuatan model.
- **Model Machine Learning**: Menggunakan XGBoost yang di-tuning untuk mendapatkan hasil prediksi terbaik. Ada juga eksperimen dengan metode ensemble untuk meningkatkan akurasi.
- **Interpretasi Model**: Menggunakan SHAP untuk mencari tahu fitur apa saja yang paling memengaruhi prediksi model.
- **Aplikasi Web**: Aplikasi sederhana yang dibuat dengan Flask untuk mencoba model yang sudah dilatih.

## Teknologi yang Dipakai

- **Bahasa**: Python
- **Library Utama**: Scikit-learn, XGBoost, SHAP, Pandas, NumPy
- **Web**: Flask

## Struktur File

```
.
├── Model Weather Prediction.ipynb  # Notebook utama untuk analisis dan modeling
├── app/
│   ├── main.py                     # Logika aplikasi web Flask
│   ├── requirements.txt            # Dependensi Python untuk aplikasi
│   ├── model/
│   │   ├── best_model.pkl          # File model yang sudah dilatih
│   │   └── scaler.pkl              # File scaler untuk data
│   ├── templates/
│   │   ├── index.html              # Halaman utama web
│   │   └── results.html            # Halaman untuk hasil prediksi
├── dataset/
│   ├── Weather Test Data.csv       # Data untuk pengujian
│   └── Weather Training Data.csv   # Data untuk melatih model
└── README.md                       # File ini
```

## Cara Menjalankan Aplikasi

Untuk menjalankan proyek ini di komputermu, ikuti langkah-langkah berikut:

### 1. Clone Repository

```bash
git clone https://github.com/bagaswibowo/XAISHAPWeatherPrediction.git
cd XAISHAPWeatherPrediction
```

### 2. Siapkan Virtual Environment

Sebaiknya gunakan virtual environment agar tidak mengubah instalasi Python di komputermu.

```bash
# Buat virtual environment
python3 -m venv venv

# Aktifkan (macOS/Linux)
source venv/bin/activate

# Untuk Windows, gunakan:
# venv\Scripts\activate
```

### 3. Instal Dependensi

Instal semua library yang dibutuhkan dari file `requirements.txt`.

```bash
pip install -r app/requirements.txt
```

### 4. Jalankan Aplikasi Web

Jalankan aplikasi dari direktori utama proyek.

```bash
python app/main.py
```

### 5. Buka Aplikasi di Browser

Buka browser dan akses alamat berikut:

**http://127.0.0.1:5001**

Sekarang Anda bisa mengunggah file data cuaca untuk mendapatkan prediksi.
