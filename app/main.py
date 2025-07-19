

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(app.root_path, 'model', 'best_model.pkl')
SCALER_PATH = os.path.join(app.root_path, 'model', 'scaler.pkl')
NUM_COLS_PATH = os.path.join(app.root_path, 'model', 'numerical_cols.pkl')
TRAIN_COLS_PATH = os.path.join(app.root_path, 'model', 'train_cols.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    if 'file' not in request.files:
        return render_template('results.html', results=None)
    file = request.files['file']
    if file.filename == '':
        return render_template('results.html', results=None)
    # Read uploaded CSV
    df = pd.read_csv(file)

    # Load model and preprocessing
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    numerical_cols = joblib.load(NUM_COLS_PATH)
    train_cols = joblib.load(TRAIN_COLS_PATH)

    # Preprocess
    X = df.copy()
    # Feature engineering (add interaction features if needed)
    if 'Humidity3pm' in X.columns and 'Pressure3pm' in X.columns:
        X['Humidity3pm_x_Pressure3pm'] = X['Humidity3pm'] * X['Pressure3pm']
    if 'Sunshine' in X.columns and 'WindGustSpeed' in X.columns:
        X['Sunshine_x_WindGustSpeed'] = X['Sunshine'] * X['WindGustSpeed']
    # Only use columns that were used for training
    X = X[train_cols]
    # Encode categorical columns (object dtype) to numeric
    for col in X.select_dtypes(include=['object']).columns:
        X[col] = X[col].astype('category').cat.codes
    X[numerical_cols] = scaler.transform(X[numerical_cols])

    # Predict
    preds = model.predict(X)
    df['Prediction'] = preds

    # Show results
    return render_template('results.html', results=df)

@app.route('/manual_predict', methods=['POST'])
def manual_predict():
    # Get manual input values from form
    min_temp = float(request.form['MinTemp'])
    max_temp = float(request.form['MaxTemp'])
    rainfall = float(request.form['Rainfall'])
    humidity3pm = float(request.form['Humidity3pm'])
    pressure3pm = float(request.form['Pressure3pm'])
    sunshine = float(request.form['Sunshine'])

    # Load model and preprocessing
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    numerical_cols = joblib.load(NUM_COLS_PATH)
    train_cols = joblib.load(TRAIN_COLS_PATH)

    # Build input DataFrame (fill missing with 0 or reasonable default)
    input_dict = {col: 0 for col in train_cols}
    input_dict['MinTemp'] = min_temp
    input_dict['MaxTemp'] = max_temp
    input_dict['Rainfall'] = rainfall
    input_dict['Humidity3pm'] = humidity3pm
    input_dict['Pressure3pm'] = pressure3pm
    input_dict['Sunshine'] = sunshine
    X = pd.DataFrame([input_dict])
    X[numerical_cols] = scaler.transform(X[numerical_cols])

    # Predict
    pred = model.predict(X)[0]
    result_df = X.copy()
    result_df['Prediction'] = pred

    return render_template('results.html', results=result_df)

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(app.root_path, 'model', 'best_model.pkl')
SCALER_PATH = os.path.join(app.root_path, 'model', 'scaler.pkl')
NUM_COLS_PATH = os.path.join(app.root_path, 'model', 'numerical_cols.pkl')
TRAIN_COLS_PATH = os.path.join(app.root_path, 'model', 'train_cols.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    if 'file' not in request.files:
        return render_template('results.html', results=None)
    file = request.files['file']
    if file.filename == '':
        return render_template('results.html', results=None)
    # Read uploaded CSV
    df = pd.read_csv(file)

    # Load model and preprocessing
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    numerical_cols = joblib.load(NUM_COLS_PATH)
    train_cols = joblib.load(TRAIN_COLS_PATH)

    # Preprocess
    X = df.copy()
    # Only use columns that were used for training
    X = X[train_cols]
    X[numerical_cols] = scaler.transform(X[numerical_cols])

    # Predict
    preds = model.predict(X)
    df['Prediction'] = preds

    # Show results
    return render_template('results.html', results=df)

if __name__ == '__main__':
    app.run(debug=True)
