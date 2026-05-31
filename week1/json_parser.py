import json

#Указываем путь к файлу с данными
file_name = "datа.json"

#Читаем файл и переводим в словарь Python + выводим возможную ошибку
try:
    with open(file_name, "r", encoding="utf-8") as file:
        data_from_json = json.load(file)
except FileNotFoundError:
    print(f"Файл '{file_name}' не найден")
    exit()

#Ищем пользователя с id>1
print("Пользователи с id > 1")
for user in data_from_json["users"]:
    if user["id"] > 1:
        print(user)

#Добавляем нового пользователя
print("\nДобавляем пользователя Chaelie")
new_user = {
    "id": 3,
    "name": "Charlie",
    "email": "charlie@example.com"
}
data_from_json["users"].append(new_user)

#Сохраняем изменения в файл
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(data_from_json, file, ensure_ascii=False, indent=4)

#Снова читаем файл и выводим всех пользователей
with open(file_name, "r", encoding="utf-8") as file:
    data_from_json = json.load(file)

print("\nСписок всех пользователей и информация о них")
for key, value in data_from_json.items():
    print(key, value)