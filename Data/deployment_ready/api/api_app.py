
from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / 'models'

app = FastAPI(title='BlueStone ML API', version='1.0.0')

class PriceRequest(BaseModel):
    property_type: str
    bedrooms: int
    bathrooms: int
    sqft: float
    lot_size: float
    year_built: int
    listing_status: str
    latitude: float
    longitude: float
    data_quality_score: float

class SLARequest(BaseModel):
    inquiry_type: str
    status: str
    inquiry_hour: int
    inquiry_dayofweek: int
    has_property_id: int
    user_type: str
    budget_mid: float | None = None
    budget_missing_flag: int = 0
    property_type: str | None = None
    bedrooms: int | None = None
    bathrooms: int | None = None
    sqft: float | None = None
    listing_status: str | None = None
    data_quality_score: float | None = None
    office_location: str | None = None
    agent_status: str | None = None
    agent_experience_years: float | None = None
    property_missing_flag: int = 0

price_model = joblib.load(MODEL_DIR / 'price_model.joblib')
sla_model = joblib.load(MODEL_DIR / 'sla_model.joblib')

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/predict/price')
def predict_price(req: PriceRequest):
    payload = pd.DataFrame([{
        'property_type': req.property_type,
        'bedrooms': req.bedrooms,
        'bathrooms': req.bathrooms,
        'sqft': req.sqft,
        'lot_size': req.lot_size,
        'year_built': req.year_built,
        'listing_status': req.listing_status,
        'latitude': req.latitude,
        'longitude': req.longitude,
        'data_quality_score': req.data_quality_score,
        'property_age': 2026 - req.year_built,
        'bed_bath_ratio': req.bedrooms / max(req.bathrooms, 1),
        'sqft_per_bedroom': req.sqft / max(req.bedrooms, 1),
        'has_valid_geo': int(-90 <= req.latitude <= 90 and -180 <= req.longitude <= 180),
    }])
    pred = price_model.predict(payload)[0]
    return {'predicted_list_price': float(pred)}

@app.post('/predict/inquiry-sla')
def predict_sla(req: SLARequest):
    payload = pd.DataFrame([req.model_dump()])
    pred = sla_model.predict(payload)[0]
    prob = None
    estimator = sla_model.named_steps['model']
    if hasattr(estimator, 'predict_proba'):
        prob = float(sla_model.predict_proba(payload)[0][1])
    return {'sla_breach_24h_prediction': int(pred), 'sla_breach_probability': prob}
