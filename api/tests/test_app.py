from http import HTTPStatus


def test_root(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"funcionou": "(/◕ヮ◕)/"}


def test_create_user(client):
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


def test_read_user(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "email": "jorge@example.com",
                "id": 1,
            }
        ]
    }


def test_delete_user(client):

    response = client.delete("/users/1")

    response.status_code == HTTPStatus.OK
    response.json() == {"message": "User deleted"}
