import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_program(client):
    # Simulate adding a program
    response = client.post('/programs', data={
        'name': 'Test Program',
        'status': 'Active',
        'color': '#ff5733'
    })
    assert response.status_code == 302  

def test_add_client(client):
    # Simulate adding a client
    response = client.post('/clients', data={
        'name': 'John Doe',
        'age': 30,
        'gender': 'Male',
        'programs': ['Test Program']
    })
    assert response.status_code == 302