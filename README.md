# BlueStone ML Project

This repository contains the end-to-end Machine Learning operations for the BlueStone project, including data processing, model training, and full API deployment code.

## Repository Structure
- `Data/`: Contains raw and processed datasets, as well as the complete deployment-ready package.
  - `Data/deployment_ready/`: The productionized API, models, and Streamlit UI code. Contains its own README for deployment instructions.
- `Notebooks/`: Contains the exploratory data analysis and ML model training Jupyter notebooks.
- `FINAL ML ARCHITECTURE/`: Contains architectural diagrams and related files.

## Deployment Package
The production deployment bundle is located in `Data/deployment_ready/`. It contains:
- `api/api_app.py`: FastAPI application serving predictions.
- `ui/streamlit_app.py`: Streamlit frontend for user interaction.
- `models/`: The trained XGBoost predictive models (`price_model.joblib` and `sla_model.joblib`).
- `Dockerfile`: Configuration to containerize the solution.
- `requirements.txt`: Python dependencies.

To run the application locally or deploy via Docker, see the detailed instructions inside `Data/deployment_ready/README.md`.
