# predict.py
import joblib
import pandas as pd

model = joblib.load("model/xgb_load_estimator.pkl")

def predict_loads(df):
    features = df[["span_m", "height_m", "width_m", "wind_kph", "snow_kpa", "occupancy"]]
    preds = model.predict(features)
    out = df.copy()
    out["Max Bending (kN·m)"] = preds[:, 0].round(1)
    out["Max Shear (kN)"]    = preds[:, 1].round(1)
    out["Deflection (mm)"]   = preds[:, 2].round(2)
    out["Safety Factor"]     = (450 / out["Max Bending (kN·m)"]).round(2)  # S355 steel
    return out
