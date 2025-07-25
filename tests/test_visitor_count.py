from fastapi.testclient import TestClient
from app.main import app
import app.routes.visitor_count as vc
from unittest.mock import patch

client = TestClient(app)

def test_visitor_count_mocked():
    with patch.object(vc, "visitor_count", 42):
        response = client.get("/api/visitor-count")
        assert response.status_code == 200
        assert response.json() == {"count": 43}