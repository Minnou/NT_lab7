from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["cinema"]

films = db["film"]
cinemas = db["cinema"]
schedule = db["schedule"]

print("\n1. Все фильмы:")
for film in films.find():
    print(film)

print("\n2. Фильм с названием 'The Case of the Smart Dummy':")
film = films.find_one({"Title": "The Case of the Smart Dummy"})
print(film)

print("\n3. Обновление названия фильма:")
films.update_one({"Film_ID": 2}, {"$set": {"Title": "The Case of the Clever Dummy"}})
print(films.find_one({"Film_ID": 2}))

print("\n4. Удаление фильма с ID = 5")
films.delete_one({"Film_ID": 5})
print(films.find_one({"Film_ID": 5}))

print("\n5. Кинотеатры с вместимостью > 500:")
for cinema in cinemas.find({"Capacity": {"$gt": 500}}):
    print(cinema)

print("\n6. Добавление нового фильма:")
new_film = {
    "Film_ID": 6,
    "Rank_in_series": 31,
    "Number_in_season": 6,
    "Title": "The Case of the Missing Script",
    "Directed_by": "New Director",
    "Original_air_date": "November 1–5, 1992",
    "Production_code": "50261–50265"
}
films.insert_one(new_film)
print(films.find_one({"Film_ID": 6}))

print("\n7. Расписание для кинотеатра с ID = 1:")
for entry in schedule.find({"Cinema_ID": 1}):
    print(entry)

print("\n8. Изменение цены билетов на 21 мая:")
schedule.update_many({"Date": "21 May"}, {"$set": {"Price": 10.99}})
for entry in schedule.find({"Date": "21 May"}):
    print(entry)

print("\n9. Удаление всех сеансов фильма с ID = 4:")
schedule.delete_many({"Film_ID": 4})
for entry in schedule.find({"Film_ID": 4}):
    print(entry)

print("\n10. Средняя цена билетов:")
pipeline = [
    {"$group": {"_id": None, "Average_Price": {"$avg": "$Price"}}}
]
result = list(schedule.aggregate(pipeline))
print(result[0]["Average_Price"] if result else "Нет данных")

print("\n11. Количество фильмов в каждом кинотеатре:")
pipeline = [
    {
        "$lookup": {
            "from": "schedule",  
            "localField": "Cinema_ID",
            "foreignField": "Cinema_ID",
            "as": "schedule_info"
        }
    },
    {
        "$project": {
            "_id": 0,
            "cinema_name": "$Name",
            "film_count": {"$size": "$schedule_info"}  
        }
    }
]

for entry in db.cinema.aggregate(pipeline):
    print(entry)

print("\n12. Средняя цена билета в каждом кинотеатре:")
pipeline = [
    {
        "$lookup": {
            "from": "schedule",
            "localField": "Cinema_ID",
            "foreignField": "Cinema_ID",
            "as": "schedule_info"
        }
    },
    {
        "$unwind": "$schedule_info"  
    },
    {
        "$group": {
            "_id": "$Name",
            "avg_price": {"$avg": "$schedule_info.Price"}  
        }
    },
    {
        "$project": {
            "_id": 0,
            "cinema_name": "$_id",
            "avg_price": 1
        }
    }
]

for entry in db.cinema.aggregate(pipeline):
    print(entry)

