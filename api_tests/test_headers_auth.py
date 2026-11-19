import requests

HTTPBIN = "https://httpbin.org"

def test_custom_header_is_sent(api_client):
    response = api_client.get(f"{HTTPBIN}/headers", headers={"X-Test-Id": "qa-123"})
    assert response.status_code == 200
    data = response.json()
    assert data["headers"]["X-Test-Id"] == "qa-123"

def test_bearer_auth_success(api_client, auth_headers):
    response = api_client.get(f"{HTTPBIN}/bearer", headers = auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert response.json()["authenticated"] is True

def test_bearer_auth_missing_token_returns_401(api_client):
    response = api_client.get(f"{HTTPBIN}/bearer")
    assert response.status_code == 401

def test_basic_auth_success(api_client):
    response = api_client.get(f"{HTTPBIN}/basic-auth/user/pass", auth=("user", "pass"))
    assert response.status_code == 200

def test_basic_auth_wrong_password_returns_401(api_client):
    response = api_client.get(f"{HTTPBIN}/basic-auth/user/pass", auth = ("user", "wrong"))
    assert response.status_code == 401

def test_response_time_is_reasonable(api_client, base_url):
    response = api_client.get(f"{base_url}/posts/1")
    assert response.elapsed.total_seconds() < 3