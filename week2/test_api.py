import requests
import pytest

def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200, f" Ожидали 200, получили {response.status_code}"
    assert "application/json" in response.headers['Content-Type'], "Неверный 'Content-Type'"
    assert "charset=utf-8" in response.headers['Content-Type'], "Неверный 'Content-Type'"

    data = response.json()
    assert "title" in data, "В ответе отсутствует поле 'title'"
    assert isinstance(data["title"], str) in data, "Поле 'title' другого типа"

    assert "userId" in data, "В ответе отсутствует поле 'id'"
    assert isinstance(data["userId"], int) in data, "Поле 'userId' другого типа"