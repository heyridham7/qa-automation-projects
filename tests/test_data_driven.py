import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    data= response.json()
    assert data["id"] == post_id

@pytest.mark.parametrize("user_id",[1,2,3])
def test_get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
