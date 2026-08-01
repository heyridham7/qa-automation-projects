import requests
import time
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_api_response_time():
    start = time.time()
    response = requests.get(f"{BASE_URL}/posts/1")
    end = time.time()

    response_time = end - start
    print(f"\nResponse time: {response_time:.2f}seconds")

    assert response.status_code == 200
    assert response_time< 2

    def test_multiple_requests_perfomance():
        times = [] 
        for i in range(5):

            start = time.time()
            response = requests.get(f"{BASE_URL}/posts/{i+1}")
            end = time.time()
            times.append(end-start)
        avg_time = sum(times)/len(times)
        print(f"\nAverage response time: {avg_time:.2f} seconds")

        assert avg_time < 2