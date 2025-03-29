from fastapi.testclient import TestClient
import logging.config
import pytest


from ctmds1.api import app

print(logging.config)


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

    cur_prices = response.json()["prices"]
    assert len(response.json()["prices"]) == 48

    # price shouldmatch from one invokation to the next
    response = client.get("/country-date/crude/2024-11-30/GB/hh")

    cur_prices2 = response.json()["prices"]
    assert response.status_code == 200
    assert cur_prices == cur_prices2
