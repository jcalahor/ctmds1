import sys
import os

from fastapi.testclient import TestClient
import pytest


sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../ctmds1"))
)

from api import app


@pytest.fixture
def client():
    # Create the TestClient with the app containing the lifespan
    with TestClient(app) as client:
        yield client


def test_market_data(client):
    response = client.get("/country-date/power/2025-01-01/DE/h")
    assert response.status_code == 200
    assert "prices" in response.json()
    assert len(response.json()["prices"]) == 24

    response = client.get("/country-date/crude/2024-11-30/GB/hh")
    assert response.status_code == 200
    assert "prices" in response.json()
    assert len(response.json()["prices"]) == 48
