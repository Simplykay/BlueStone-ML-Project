
from pathlib import Path
import joblib
import pandas as pd
import shap

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / 'models'
price_model = joblib.load(MODEL_DIR / 'price_model.joblib')

def run_price_shap(sample_df: pd.DataFrame):
    transformed = price_model.named_steps['preprocessor'].transform(sample_df)
    model = price_model.named_steps['model']
    explainer = shap.TreeExplainer(model)
    return explainer.shap_values(transformed)
