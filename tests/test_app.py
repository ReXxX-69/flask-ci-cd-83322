import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_83322(client):
    rv = client.get('/')
    assert rv.data == b'Kacper_Jamrozinski_83322'
