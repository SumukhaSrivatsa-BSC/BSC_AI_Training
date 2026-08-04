from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_note():
    payload = {"id": 1, "title": "First", "body": "Hello"}
    created = client.post("/notes", json=payload)
    assert created.status_code == 201
    assert created.json() == payload

    fetched = client.get("/notes/1")
    assert fetched.status_code == 200
    assert fetched.json()["title"] == "First"


def test_missing_note_returns_404():
    response = client.get("/notes/999")
    assert response.status_code == 404
