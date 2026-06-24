from http import HTTPStatus

from fastapi.testclient import TestClient

from viajei_api.app import app


def test_root():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"funcionou": "(/◕ヮ◕)/"}


def test_create_user():
    client = TestClient(app)

    response = client.post(
        "/auth/",
        json={
            "email": "jorge@example.com",
            "password": "secret",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "email": "jorge@example.com",
        "id": 1,
    }
