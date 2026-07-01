import requests
import pytest

#Фикстура для базового url
@pytest.fixture
def base_url():
    return 'https://jsonplaceholder.typicode.com'

#Параметризация для проверки нескольких постов
@pytest.mark.parametrize('post_id', [1, 2, 3])
def test_multiple_posts(base_url, post_id):
    response = requests.get(f'{base_url}/posts/{post_id}')
    assert response.status_code == 200


def test_get_post(base_url):
#Проверка метода GET /posts/1
    response = requests.get(f'{base_url}/posts/1')

    assert response.status_code == 200, f" Ожидали 200, получили {response.status_code}"
    assert "application/json" in response.headers['Content-Type'], "Неверный 'Content-Type'"
    assert "charset=utf-8" in response.headers['Content-Type'], "Неверный 'Content-Type'"

    data = response.json()
    assert "title" in data, "В ответе отсутствует поле 'title'"
    assert isinstance(data["title"], str) , "Поле 'title' другого типа"

    assert "userId" in data, "В ответе отсутствует поле 'userId'"
    assert isinstance(data["userId"], int), "Поле 'userId' другого типа"

def test_get_users(base_url):
# Проверка метода GET /users
    response = requests.get(f'{base_url}/users')

    assert response.status_code == 200, f" Ожидали 200, получили {response.status_code}"
    users = response.json()
    assert len(users) > 0, "Список пользователей пуст"
    assert "name" in users[1], "Имя пользователя отсутствует"
    assert "email" in users[1], "Почта пользователя отсутствует"

def test_create_new_post(base_url):
# Проверка метода /posts
    first_test = {
        "title": "Новый юзер",
        "body": "Валентин",
        "userId": 1
    }
    response = requests.post(f'{base_url}/posts', json=first_test)

    assert response.status_code == 201, f"Ожидали 201, получили {response.status_code}"
    users = response.json()
    assert 'id' in users, "'id' отсутствует в ответе"
    assert isinstance(users['title'], str), "Поле 'title' другого типа"
    assert users["title"] == first_test["title"], "В ответе другое значение 'title'"

def test_non_existent_post(base_url):

    response = requests.post(f'{base_url}/posts/999')
    assert response.status_code == 404, f" Ожидали 404, получили {response.status_code}"

