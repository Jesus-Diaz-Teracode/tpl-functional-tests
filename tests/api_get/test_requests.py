import pytest

from .fixtures import http_client, headers, payload

def test_google(http_client, headers, payload):
    http_client.headers = headers
    http_client.payload = payload

    r = http_client
    assert r.status_code == 200