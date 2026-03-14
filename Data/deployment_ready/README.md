
# BlueStone Deployment Ready Package

## Contents
- models/price_model.joblib
- models/sla_model.joblib
- api/api_app.py
- ui/streamlit_app.py
- scripts/shap_utils.py
- requirements.txt
- Dockerfile

## Run API locally
```bash
cd deployment_ready
pip install -r requirements.txt
uvicorn api.api_app:app --reload
```

Open docs:
http://127.0.0.1:8000/docs

## Run Streamlit UI
```bash
streamlit run ui/streamlit_app.py
```

## Run MLflow UI
```bash
mlflow ui
```

## Docker build
```bash
docker build -t bluestone-ml-api .
docker run -p 8000:8000 bluestone-ml-api
```
