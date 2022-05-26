from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_read_list():
    response = client.get("/list")
    assert response.status_code == 200

def test_read_query():
    response = client.get("/query/?q=公園")
    assert response.status_code == 200

def test_read_version():
    response = client.get("/version")
    assert response.status_code == 200

