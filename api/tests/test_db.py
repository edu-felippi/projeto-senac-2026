from sqlalchemy import select

from viajei_api.models import User


def test_create_user(session):
    new_user = User(email="jorge@example.test", password="SenhaForte123")

    session.add(new_user)
    session.commit()

    user = session.scalar(
        select(User).where(User.email == "jorge@example.test")
    )

    assert user.email == "jorge@example.test"
