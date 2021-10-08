from server import __version__
from fastapi.testclient import TestClient
from server.main import app

client = TestClient(app)


def test_version():
    assert __version__ == "0.1.0"


def test_authorization():
    response = client.get("/get_all/")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
