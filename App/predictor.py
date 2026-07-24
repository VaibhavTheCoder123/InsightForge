import joblib
import pandas as pd

MODEL_PATH = "../models/logistic_regression_model.pkl"
SCALER_PATH = "../models/scaler.pkl"
COLUMNS_PATH = "../models/columns.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
columns = joblib.load(COLUMNS_PATH)


def preprocess_input(user_data):

    df = pd.DataFrame([user_data])

    df = pd.get_dummies(df)

    df = df.reindex(columns=columns, fill_value=0)

    df_scaled = scaler.transform(df)

    return df_scaled


def predict_churn(user_data):

    processed = preprocess_input(user_data)

    prediction = model.predict(processed)[0]

    probability = model.predict_proba(processed)[0][1]

    return prediction, probability