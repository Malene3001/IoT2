import sqlite3 as sql
from time import sleep
from random import randint

con = sql.connect('db_statistics.db')

cur = con.cursor()

sql = '''CREATE TABLE TemperatureANDHumidity (
"Temperature"  NUMERIC,
"Humidity" NUMCERIC,
"Time" DATETIME
)'''

def insertData():
    query = "INSERT INTO TemperatureANDHumidity(Temperature, Humidity, Time) VALUES(datetime('now'), ?, ?) "
    Temperature = randint(10,40)
    Humidity = randint(10, 40)
    data = (Temperature, Humidity)
    with con:
        cur = con.cursor()
        cur.execute(query, data)
while True:
    insertData()
    sleep(3)