from app import app

def test_root_returns_greeting():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    text = resp.data.decode("utf-8", errors="ignore")
    assert "Hola" in text
    assert "Entregable 4" in text
