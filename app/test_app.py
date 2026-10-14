from app import app

def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.get_json()["service"] == "gke-gitops-platform"

def test_health():
    assert app.test_client().get("/healthz").status_code == 200

def test_ready():
    assert app.test_client().get("/readyz").status_code == 200
