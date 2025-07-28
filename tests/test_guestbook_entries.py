from fastapi.testclient import TestClient
from app.main import app
import app.routes.guestbook_entries as ge
from unittest.mock import patch, mock_open
import json

client = TestClient(app)

mock_data = json.dumps([
    {"name": "JohnDoe", "message": "Hello, world!"}
])

def test_get_guestbook_entries():
    with patch("app.routes.guestbook_entries.open", mock_open(read_data=mock_data)):
        response = client.get("/api/guestbook-entries")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert response.json()[0]["name"] == "JohnDoe"
        assert response.json()[0]["message"] == "Hello, world!"

def test_get_guestbook_entries_no_data():
    with patch("app.routes.guestbook_entries.open", mock_open(read_data="[]")):
        response = client.get("/api/guestbook-entries")
        assert response.status_code == 200
        assert response.json() == {
            "code": "DATA_UNAVAILABLE",
            "message": "No guestbook entries found."
        }