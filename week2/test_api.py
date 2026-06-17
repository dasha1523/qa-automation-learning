import requests
import pytest

def test_get_post():
#Проверка метода GET /posts/1
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200, f" Ожидали 200, получили {response.status_code}"
    assert "application/json" in response.headers['Content-Type'], "Неверный 'Content-Type'"
    assert "charset=utf-8" in response.headers['Content-Type'], "Неверный 'Content-Type'"

    data = response.json()
    assert "title" in data, "В ответе отсутствует поле 'title'"
    assert isinstance(data["title"], str) , "Поле 'title' другого типа"

    assert "userId" in data, "В ответе отсутствует поле 'userId'"
    assert isinstance(data["userId"], int), "Поле 'userId' другого типа"

def test_get_users():
# Проверка метода GET /users
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)

    assert response.status_code == 200, f" Ожидали 200, получили {response.status_code}"
    users = response.json()
    assert len(users) > 0, "Список пользователей пуст"
    assert "name" in users[1], "Имя пользователя отсутствует"
    assert "email" in users[1], "Почта пользователя отсутствует"

def test_create_new_post():
# Проверка метода /posts
    first_test = {
        "title": "Новый юзер",
        "body": "Валентин",
        "userId": 1
    }
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.post(url, json=first_test)

    assert response.status_code == 201, f"Ожидали 200, получили {response.status_code}"
    users = response.json()
    assert 'id' in users, "'id' отсутствует в ответе"
    assert isinstance(users['title'], str), "Поле 'title' другого типа"
    assert users["title"] == first_test["title"], "В ответе другое значение 'title'"

def test_non_existent_post():

    response = requests.post('https://jsonplaceholder.typicode.com/posts/999')
    assert response.status_code == 404, f" Ожидали 404, получили {response.status_code}"

