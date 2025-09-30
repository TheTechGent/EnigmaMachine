import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_main():
    """Test the main endpoint serves the frontend."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_encrypt_endpoint_basic():
    """Test basic encryption endpoint."""
    payload = {
        "message": "HELLO",
        "rotor1": "I",
        "rotor2": "II",
        "rotor3": "III",
        "reflector": "B",
        "position": "AAA",
        "rings": [1, 1, 1],
        "plugboard": [],
    }

    response = client.post("/api/encrypt", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "encrypted_message" in data
    assert len(data["encrypted_message"]) == len(payload["message"])


def test_encrypt_endpoint_invalid_rotor():
    """Test encryption with invalid rotor configuration."""
    payload = {
        "message": "HELLO",
        "rotor1": "INVALID",
        "rotor2": "II",
        "rotor3": "III",
        "reflector": "B",
        "position": "AAA",
        "rings": [1, 1, 1],
        "plugboard": [],
    }

    response = client.post("/api/encrypt", json=payload)
    assert response.status_code == 400


def test_encrypt_endpoint_empty_message():
    """Test encryption with empty message."""
    payload = {
        "message": "",
        "rotor1": "I",
        "rotor2": "II",
        "rotor3": "III",
        "reflector": "B",
        "position": "AAA",
        "rings": [1, 1, 1],
        "plugboard": [],
    }

    response = client.post("/api/encrypt", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["encrypted_message"] == ""


def test_encrypt_endpoint_with_plugboard():
    """Test encryption with plugboard connections."""
    payload = {
        "message": "HELLO",
        "rotor1": "I",
        "rotor2": "II",
        "rotor3": "III",
        "reflector": "B",
        "position": "AAA",
        "rings": [1, 1, 1],
        "plugboard": ["AB", "CD", "EF"],
    }

    response = client.post("/api/encrypt", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "encrypted_message" in data


def test_health_endpoint():
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "healthy"


def test_machine_config_endpoint():
    """Test getting machine configuration."""
    response = client.get("/api/config")
    assert response.status_code == 200

    data = response.json()
    assert "rotors" in data
    assert "reflectors" in data
    assert "I" in data["rotors"]
    assert "B" in data["reflectors"]


def test_encrypt_endpoint_missing_fields():
    """Test encryption with missing required fields."""
    payload = {
        "message": "HELLO"
        # Missing other required fields
    }

    response = client.post("/api/encrypt", json=payload)
    assert response.status_code == 422  # Validation error


def test_static_files():
    """Test that static files are served correctly."""
    response = client.get("/static/style.css")
    assert response.status_code == 200
    assert "text/css" in response.headers["content-type"]

    response = client.get("/static/script.js")
    assert response.status_code == 200
    assert "javascript" in response.headers["content-type"]
