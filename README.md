# 🌦️ Prediksi Cuaca Australia dengan XGBoost, SHAP, dan Flask

Proyek ini adalah sebuah pipeline machine learning lengkap untuk memprediksi kemungkinan hujan di Australia pada hari berikutnya. Pipeline ini mencakup analisis data eksplorasi (EDA), preprocessing, pelatihan model, tuning hyperparameter, hingga interpretasi model menggunakan SHAP. Hasil akhirnya adalah sebuah aplikasi web sederhana yang dibangun dengan Flask, di mana pengguna dapat mengunggah data cuaca dalam format CSV atau Excel untuk mendapatkan prediksi.

## 🚀 Fitur Utama

- **Analisis Data Komprehensif**: Notebook Jupyter (`Model Weather Prediction.ipynb`) menyajikan analisis data yang mendalam, mulai dari pembersihan, visualisasi, hingga analisis korelasi.
- **Modeling dengan XGBoost**: Menggunakan `XGBoost`, salah satu algoritma gradient boosting terkuat, untuk mencapai akurasi prediksi yang tinggi.
- **Tuning Hyperparameter**: Melakukan optimisasi model menggunakan `GridSearchCV` dan `RandomizedSearchCV` untuk menemukan parameter terbaik.
- **Ensemble Learning**: Menerapkan metode `StackingClassifier` yang menggabungkan beberapa model (XGBoost, RandomForest, LogisticRegression) untuk meningkatkan performa.
- **Interpretasi Model dengan SHAP**: Menganalisis "kotak hitam" model dengan SHAP (SHapley Additive exPlanations) untuk memahami faktor-faktor utama yang memengaruhi prediksi.
- **Aplikasi Web Interaktif**: Sebuah aplikasi web berbasis Flask yang memungkinkan pengguna mengunggah file data mereka sendiri dan mendapatkan prediksi secara real-time.
- **Modular dan Terdokumentasi**: Kode ditulis secara modular dan setiap langkah dalam notebook dijelaskan dengan baik untuk kemudahan pemahaman.

## 🛠️ Teknologi yang Digunakan

- **Bahasa Pemrograman**: Python 3
- **Library Machine Learning**: Scikit-learn, XGBoost, SHAP
- **Analisis & Manipulasi Data**: Pandas, NumPy
- **Visualisasi Data**: Matplotlib, Seaborn
- **Web Framework**: Flask
- **Deployment Lokal**: Virtual Environment Python

## 📂 Struktur File

```
.
├── Model Weather Prediction.ipynb  # Notebook utama untuk analisis dan modeling
├── Weather Improve Prediction.ipynb # Notebook pengembangan (opsional)
├── app/
│   ├── main.py                     # Logika aplikasi web Flask
│   ├── requirements.txt            # Dependensi Python untuk aplikasi
│   ├── model/
│   │   ├── best_model.pkl          # File model terbaik yang disimpan
│   │   ├── scaler.pkl              # File scaler yang disimpan
│   │   ├── numerical_cols.pkl      # Daftar kolom numerik
│   │   └── train_cols.pkl          # Daftar semua kolom training
│   ├── templates/
│   │   ├── index.html              # Halaman utama aplikasi web
│   │   └── results.html            # Halaman untuk menampilkan hasil prediksi
│   └── uploads/                    # Folder untuk menyimpan file yang diunggah
├── dataset/
│   ├── Weather Test Data.csv       # Data uji
│   └── Weather Training Data.csv   # Data latih
└── README.md                       # File ini
```

## ⚙️ Instalasi & Cara Menjalankan

Untuk menjalankan proyek ini di lingkungan lokal Anda, ikuti langkah-langkah berikut:

### 1. Clone Repository

```bash
git clone <URL_REPOSITORY_ANDA>
cd <NAMA_FOLDER_REPO>
```

### 2. Buat dan Aktifkan Virtual Environment

Sangat disarankan untuk menggunakan virtual environment agar tidak mengganggu instalasi Python global Anda.

```bash
# Membuat virtual environment
python3 -m venv venv

# Mengaktifkan virtual environment (macOS/Linux)
source venv/bin/activate

# Untuk Windows, gunakan:
# venv\Scripts\activate
```

### 3. Instal Dependensi

Instal semua library yang dibutuhkan menggunakan file `requirements.txt` yang ada di dalam folder `app`.

```bash
pip install -r app/requirements.txt
```

### 4. Jalankan Aplikasi Web Flask

Setelah semua dependensi terinstal, jalankan aplikasi web dari direktori utama proyek.

```bash
python app/main.py
```

### 5. Akses Aplikasi

Buka browser web Anda dan navigasikan ke alamat berikut:

**http://127.0.0.1:5001**

Anda akan melihat halaman utama di mana Anda dapat mengunggah file `Weather Test Data.csv` atau file data cuaca lainnya yang memiliki format serupa untuk mendapatkan prediksi.
