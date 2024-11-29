from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_root() -> None:
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"state" : "Server up running!!"}
