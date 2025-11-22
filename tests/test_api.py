from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_and_docs():
    response = client.get("/")
    assert response.status_code == 200

    docs = client.get("/docs")
    assert docs.status_code == 200

def test_recommendations_exist():
    client.post("/users", json={"id": 1, "name": "Marco"})

    client.post("/items", json={"id": 1, "title": "Toy Story"})

    client.put("/ratings", json={"user_id": 1, "item_id": 1, "rating": 5})

    response = client.get("/recommendations/1?n=5")
    assert response.status_code == 200
    assert "recommendations" in response.json()
