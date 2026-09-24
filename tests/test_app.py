from app import app


def test_get_users():
    client = app.test_client()

    response = client.get("/api/users")

    assert response.status_code == 200