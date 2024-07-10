import logging.config

from fastapi.testclient import TestClient

from src.app.common.variables import config_log
from src.app.example import app as test_app


logging.config.dictConfig(config_log)
logger = logging.getLogger(__name__)


client = TestClient(app=test_app)


def test_function():
    response = client.post("/api/v1/example/ex1")
    assert response.status_code == 200
    assert response.json() == {"example": "example"}


def test_healthcheck():
    response = client.get("/api/v1/healthcheck")
    assert response.status_code == 200
    assert response.json() == {'healthcheck': 'success'}
