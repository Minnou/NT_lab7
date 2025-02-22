import json
from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["cinema"]  # Создаём/подключаемся к базе данных

# Загружаем JSON-данные из файла
with open("db/cinema.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Импорт данных в коллекции
db["film"].insert_many(data["film"])
db["cinema"].insert_many(data["cinema"])
db["schedule"].insert_many(data["schedule"])

print("Данные загружены")