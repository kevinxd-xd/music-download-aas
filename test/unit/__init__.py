import pytest

from flaskr.main import app

@pytest.fixture
def client():
    client = app.test_client()

    yield client