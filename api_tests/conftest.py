import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_client():
    session = requests.Session()
    session.headers.update({"Content-Type":"application/json; charset=UTF-8"})
    yield session
    session.close()

@pytest.fixture
def auth_headers():
    return {"Authorization": "Bearer my-test-token"}