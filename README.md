# Prediksi Cuaca Australia

Proyek ini memprediksi apakah besok akan hujan di Australia menggunakan pipeline machine learning XGBoost, GridSearchCV, SHAP, dan Flask web app. Semua proses mulai dari analisis data, training, interpretasi, hingga deployment web dijelaskan dan diimplementasikan secara modular.

## Fitur Proyek

- **Notebook Analisis**: `Model Weather Prediction.ipynb` berisi seluruh workflow:
  - Analisis data, EDA, preprocessing, feature engineering
  - Training & tuning model (XGBoost, GridSearchCV, ensemble)
  - Evaluasi, interpretasi SHAP, validasi manual
  - Penyimpanan model, scaler, dan kolom fitur untuk aplikasi web
- **Aplikasi Web**: Flask app yang bisa:
  - Upload file CSV (contoh: Weather Test Data.csv) untuk prediksi batch
  - Input manual data cuaca untuk prediksi satu baris
  - Tampilkan hasil prediksi dalam bentuk tabel
- **Model & Scaler**: Model terbaik, scaler, dan daftar kolom fitur disimpan otomatis dari notebook ke folder `app/model/` agar bisa langsung dipakai di web.

## Teknologi

- **Bahasa**: Python
- **Library Utama**: scikit-learn, xgboost, shap, pandas, numpy, matplotlib, seaborn
- **Web**: Flask

## Struktur File

```
.
├── Model Weather Prediction.ipynb      # Notebook utama analisis, training, interpretasi, dan export model
├── app/
│   ├── main.py                        # Logika aplikasi web Flask
│   ├── requirements.txt               # Dependensi Python untuk aplikasi web
│   ├── model/
│   │   ├── best_model.pkl             # Model machine learning terlatih
│   │   ├── scaler.pkl                 # Scaler untuk fitur numerik
│   │   ├── train_cols.pkl             # Daftar kolom fitur yang digunakan saat training
│   │   └── numerical_cols.pkl         # Daftar kolom numerik yang di-scale
│   ├── templates/
│   │   ├── index.html                 # Halaman utama web (upload & input manual)
│   │   └── results.html               # Halaman hasil prediksi
├── dataset/
│   ├── Weather Test Data.csv          # Data untuk pengujian
│   └── Weather Training Data.csv      # Data untuk melatih model
└── README.md                          # File ini
```

## Cara Menjalankan Proyek

### 1. Clone Repository

```bash
git clone https://github.com/bagaswibowo/XAISHAPWeatherPrediction.git
cd XAISHAPWeatherPrediction
```

### 2. Siapkan Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
```

### 3. Instal Dependensi

```bash
pip install -r app/requirements.txt
```

### 4. Jalankan Aplikasi Web

```bash
python app/main.py
```

### 5. Buka Aplikasi di Browser

Buka browser dan akses:

**http://127.0.0.1:5000**

### 6. Fitur Web

- **Upload CSV**: Unggah file data cuaca (misal: Weather Test Data.csv) untuk prediksi batch.
- **Input Manual**: Isi data cuaca secara manual di form untuk prediksi satu baris.
- **Hasil Prediksi**: Tampil dalam bentuk tabel, bisa diunduh atau disalin.

### 7. Export Model dari Notebook

Di akhir notebook, model terbaik, scaler, dan daftar kolom fitur otomatis disimpan ke folder `app/model/`:

```python
import joblib
joblib.dump(final_model, 'app/model/best_model.pkl')
joblib.dump(scaler, 'app/model/scaler.pkl')
joblib.dump(num_cols, 'app/model/numerical_cols.pkl')
joblib.dump(X_train.columns.tolist(), 'app/model/train_cols.pkl')
```

## Catatan

- Pastikan file model dan scaler sudah di-export dari notebook sebelum menjalankan web.
- Jika ingin menambah fitur input manual, tambahkan field di `index.html` dan update backend di `main.py`.
- Untuk interpretasi model dan analisis SHAP, lihat penjelasan dan visualisasi di notebook.
