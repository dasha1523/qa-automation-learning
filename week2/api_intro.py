import requests

#Задание 1: Разведка боем (просто GET)
print("Задание 1")
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
#Получаем значение заголовка 'Content-Type'
content_type = response.headers['Content-Type']

#Выводим код ответа
print(f" Код ответа: {response.status_code}")
#Выводим заголовок "Content-Type"
print(f" Заголовок 'Content-Type': {content_type}")
data = response.json()
#Выводим заголовок "title"
print(data['title'])



#Задание 2: Список пользователей
print("Задание 2")
response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()
#Выводим имена и почты пользователей
for user in users:
    print(f" Имя: {user['name']}")
    print(f" Email: {user['email']}")

# Задание 3: Создание поста (POST)
print("Задание 3")

first_test = {
    "title": "Мой автотест",
    "body": "Этот пост создан автоматически",
    "userId": 1
}

response = requests.post ('https://jsonplaceholder.typicode.com/users', json=first_test)

# Проверяем, что ответ от сервера равен 201. Выводим ошибку в том случае, если ответ от сервера НЕ равен 201
try:
    assert response.status_code == 201
except requests.exceptions.HTTPError as e:
    print(f" HTTP ошибка: {e.response.status_code}")

# Выводим id пользователя
users = response.json()
print (f" id пользователя равно {users['id']}")

# Словарь, для себя, чтобы смотреть ошибки
# help(requests.exceptions)

# Задание 4: Обработка ошибок
print("Задание 4")
response = requests.get('https://jsonplaceholder.typicode.com/posts/999')
if response.status_code == 404:
    print("Пост не найден")
else:
    print("Что-то пошло не так")
