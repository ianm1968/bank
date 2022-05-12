"""Integration tests for app.py"""
from typing import Type
from flask.testing import FlaskClient
from flask.wrappers import Response
import pytest

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation(client: FlaskClient):
    # Use the client to make requests e.g.:
    something = client.post('/accounts/Fred Bloggs')
    assert something.status_code == 200

def test_account_creation_then_get(client: FlaskClient):
    # Use the client to make requests e.g.:
    something = client.post('/accounts/Fred Bloggs')
    something = client.get('/accounts/Fred Bloggs')
    assert something.status_code == 200


def test_account_get_without_creation(client: FlaskClient):
    # Use the client to make requests e.g.:
    something = client.get('/accounts/Fred Bloggs')
    assert something.status_code == 404
