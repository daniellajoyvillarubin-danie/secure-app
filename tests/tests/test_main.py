import pytest
from app.main import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
         yield client


def test_health_check(client):
   response = client.get('/health')
      assert response.status_code == 200
      assert response.json['status'] == 'healthy'


def test_add_numbers_success(client):
      payload = {
         "a": 10,
         "b": 5

  }

     response = client.post('/add', json=payload)

    assert response.status_code == 200
    assert response.json['result'] == 15

def test_add_numbers_invalid_input(client):
    payload = {
       "a": "hello",
       "b": 5
                                                                      
}

    response = client.post('/add', json=payload)

    assert response.status_code == 40 8