import json

with open("data.json.py", "r", encoding="utf-8") as b:
    data_from_json = json.load(b)

for user in data_from_json["users"]:
    if user["id"] > 1:
        print(user)

new_user = {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
data_from_json["users"].append(new_user)

with open("data.json.py", "w", encoding="utf-8") as f:
    json.dump(data_from_json, f, ensure_ascii=False, indent=4)

with open("data.json.py", "r", encoding="utf-8") as b:
    data_from_json = json.load(b)

for key, value in data_from_json.items():
    print(key, value)