import pytest
from app.config import settings
from httpx import Client
from app.main import app as fastapi_app
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def prepare():
    assert settings.MODE == 'TEST'


@pytest.fixture(scope='function')
def cl():
    with TestClient(app=fastapi_app, base_url='http://test') as cl:
        yield cl
