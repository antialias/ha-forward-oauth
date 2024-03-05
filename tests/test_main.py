import requests_mock
import pytest
from flask import url_for
from app.main import app as flask_app  # Ensure this import matches the structure of your project

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Note: If your app factory needs arguments, adjust as necessary
    app = flask_app
    app.config.update({"TESTING": True, "SECRET_KEY": "for test purposes"})
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_auth_redirect(client):
    """Test the /auth route redirects to Home Assistant's OAuth page."""
    response = client.get('/auth')
    assert response.status_code == 302
    assert "localhost:8123" in response.headers["Location"]

def test_auth_success(client):
    """Test successful authentication redirects to /auth_success."""
    # Mock or simulate successful authentication here, possibly by setting session variables directly if necessary
    # This is just a conceptual example; adjust based on how your authentication flow is implemented
    response = client.get('/auth_success')
    assert response.status_code == 200
    assert b"Successfully authenticated with Home Assistant" in response.data

def test_callback_failure(client):
    with requests_mock.Mocker() as m:
        m.post("http://localhost:8123/auth/token", status_code=401)
        response = client.get('/callback', query_string={"code": "invalid"})
        assert response.status_code == 401
        assert b"Failed to authenticate" in response.data

