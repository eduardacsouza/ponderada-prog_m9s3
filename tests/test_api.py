import pytest
from fastapi.testclient import TestClient
from ..src.services.api import app

client = TestClient(app)

def test_start_playback_success():
    response = client.post("/playback/start/", json={"user_id": 1, "video_id": "abc123"})
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_start_playback_invalid_user():
    response = client.post("/playback/start/", json={"user_id": None, "video_id": "abc123"})
    assert response.status_code == 400

def test_start_playback_invalid_video():
    response = client.post("/playback/start/", json={"user_id": 1, "video_id": ""})
    assert response.status_code == 400
