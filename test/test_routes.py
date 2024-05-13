import pytest
from app import create_app
from flask import json

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_comments(client):
    response = client.get('/comments?subfeddit=general')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert 'id' in data[0]
    assert 'text' in data[0]
    assert 'polarity' in data[0]
    assert 'classification' in data[0]
