import pytest
from main import app

@pytest.fixture

def client():
    app.testing = True
    with app.test_client() as client:
        yield client
        
def test_home(client):
    response = client.get("/")
    # To test post
    # response2 = client.post("/add-user", json={"username": "test"})
    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Hello Flask"
    }
