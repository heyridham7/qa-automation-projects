import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post_status_code():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_get_post_user_id():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "userId" in data
 
def test_get_post_title_is_string():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert isinstance(data["title"],str)

def test_get_all_points_return_100():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert len(data) == 100

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert data["id"]==1
    assert "email" in data
 