import sqlite3

db = sqlite3.connect("bikes.db")
db.isolation_level = None

def distance_of_user(user):
    distance = db.execute("""SELECT SUM(distance) FROM Trips
    JOIN Users ON Trips.user_id = Users.id
    WHERE Users.name = ?""", (user,)).fetchone()
    return distance
    