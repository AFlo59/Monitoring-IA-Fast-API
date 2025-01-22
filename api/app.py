# api/app.py

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="ML Iris API",
    description="API de prédiction Iris avec monitoring Prometheus",
    version="1.0.0",
)

# Chargement du modèle
model = joblib.load("model.pkl")

# Classe pour définir le payload attendu dans /predict
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Endpoint de prédiction
@app.post("/predict")
def predict(iris: IrisFeatures):
    # Conversion de la requête en numpy array
    features = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]])
    prediction = model.predict(features)
    return {
        "prediction": int(prediction[0])
    }

# Instrumentation Prometheus
# - On initialise l'instrumentation à la création de l'app
@app.on_event("startup")
async def _startup():
    Instrumentator().instrument(app).expose(app, include_in_schema=False, endpoint="/metrics")