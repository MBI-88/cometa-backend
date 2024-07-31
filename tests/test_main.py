from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_get_beers():
    response = client.get("/api/beers")
    assert response.status_code == 200
    assert len(response.content) >= 100

def test_get_order():
    response = client.get("/api/order")
    assert response.status_code == 200
    assert len(response.content) >= 100
