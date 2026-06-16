import requests
import pytest

def_test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200, f" Ожидали 200, получили {response.status_code}"