from backend.sample_app import sample

def test_api_responde_200():
    client = sample.test_client()
    response = client.get("/api")


    assert response.status_code == 200 # nosec B101
    assert response.get_json()["mensaje"] == "API funcionando correctamente" # nosec B101