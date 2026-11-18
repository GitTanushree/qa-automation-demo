import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_single_post():
	response = requests.get(f"{BASE_URL}/posts/1")
	assert response.status_code == 200
	data = response.json()
	assert data["id"] == 1
	assert data["userId"] == 1
	assert "title" in data

def test_get_all_posts():
	response = requests.get(f"{BASE_URL}/posts")
	assert response.status_code == 200
	data = response.json()
	assert len(data) == 100

def test_create_post():
	payload = {"title":"QA practice", "body": "Testing POST", "userId":1}
	response = requests.post(f"{BASE_URL}/posts",json=payload)
	assert response.status_code == 201
	data = response.json()
	assert data["title"] == payload["title"]
	assert data["body"] == payload["body"]
	assert data["userId"] == payload["userId"]
	assert "id" in data

def test_get_nonexistent_post():
	response = requests.get(f"{BASE_URL}/posts/9999")
	assert response.status_code == 404