import pytest

@pytest.mark.parametrize("post_id", [1,2,50,100])
def test_get_post_by_id(api_client, base_url, post_id):
    response = api_client.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id


@pytest.mark.parametrize("userId", [1,2,10])
def test_posts_filtered_by_user(api_client, base_url, userId):
    response = api_client.get(f"{base_url}/posts", params = {"userId":userId})
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) == 10
    assert all(p["userId"] == userId for p in posts)

@pytest.mark.parametrize("bad_id",[0,101,9999])
def test_get_invalid_posts_return_404(api_client, bad_id, base_url):
    response = api_client.get(f"{base_url}/posts/{bad_id}")
    assert response.status_code == 404


                              
