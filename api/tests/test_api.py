# File: api/tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={"feature1": 1.0, "feature2": 2.0, "feature3": 3.0})
    assert response.status_code == 200
    assert "prediction" in response.json()