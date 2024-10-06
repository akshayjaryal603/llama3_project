from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_book():
    response = client.post("/books", json={"title": "Book1", "author": "Author1"})
    assert response.status_code == 200
