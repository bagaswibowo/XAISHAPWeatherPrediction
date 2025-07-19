# Prediksi Cuaca Australia

Proyek ini memprediksi apakah besok akan hujan di Australia menggunakan pipeline machine learning (XGBoost, GridSearchCV, SHAP) dan aplikasi web Flask.

## Fitur Utama

- Analisis data, EDA, preprocessing, feature engineering, training, tuning, dan interpretasi model di notebook.
- Export model, scaler, dan kolom fitur dari notebook ke folder `app/model/`.
- Web Flask untuk prediksi cuaca:
  - Upload file CSV (Weather Test Data.csv) untuk prediksi batch.
  - Input manual data cuaca untuk prediksi satu baris.
  - Hasil prediksi tampil dalam tabel.

## Struktur File

```
├── Model Weather Prediction.ipynb      # Notebook analisis, training, interpretasi, export model
├── app/
│   ├── main.py                        # Web Flask
│   ├── requirements.txt               # Dependensi web
│   ├── model/
│   │   ├── best_model.pkl             # Model terlatih
│   │   ├── scaler.pkl                 # Scaler fitur numerik
│   │   ├── train_cols.pkl             # Daftar kolom fitur
│   │   └── numerical_cols.pkl         # Daftar kolom numerik
│   ├── templates/
│   │   ├── index.html                 # Halaman utama (upload & input manual)
│   │   └── results.html               # Halaman hasil prediksi
├── dataset/
│   ├── Weather Test Data.csv          # Data pengujian
│   └── Weather Training Data.csv      # Data training
└── README.md
```

## Cara Menjalankan

1. Clone repository dan masuk ke folder proyek:
   ```bash
   git clone https://github.com/bagaswibowo/XAISHAPWeatherPrediction.git
   cd XAISHAPWeatherPrediction
   ```
2. Buat dan aktifkan virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # venv\Scripts\activate   # Windows
   ```
3. Install dependensi:
   ```bash
   pip install -r app/requirements.txt
   ```
4. Jalankan aplikasi web:
   ```bash
   python app/main.py
   ```
5. Buka browser ke:
   ```
   http://127.0.0.1:5000
   ```

## Fitur Web

- **Upload CSV**: Prediksi batch dari file cuaca.
- **Input Manual**: Prediksi satu baris dari form input.
- **Hasil Prediksi**: Tabel hasil prediksi, bisa diunduh/disalin.

## Export Model dari Notebook

Di akhir notebook, simpan model, scaler, dan kolom fitur ke folder `app/model/`:

```python
import joblib
joblib.dump(final_model, 'app/model/best_model.pkl')
joblib.dump(scaler, 'app/model/scaler.pkl')
joblib.dump(num_cols, 'app/model/numerical_cols.pkl')
joblib.dump(X_train.columns.tolist(), 'app/model/train_cols.pkl')
```

## Catatan

- Pastikan file model dan scaler sudah diekspor dari notebook sebelum menjalankan web.
- Untuk interpretasi model dan analisis SHAP, lihat penjelasan di notebook.
