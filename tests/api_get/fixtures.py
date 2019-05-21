import pytest
import requests

@pytest.fixture
def headers():
    return {'Content-Type': 'application/json'}

@pytest.fixture
def payload():
    return {'foo': 'bar'}

@pytest.fixture
def http_client():
    return requests.get('https://www.google.com')