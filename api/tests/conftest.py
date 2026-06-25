import pytest
from fastapi.testclient import TestClient

from viajei_api.app import app


@pytest.fixture
def client():
    return TestClient(app)
