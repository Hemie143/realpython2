import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    cars = [
        ('Ford', 'Bronco', 42),
        ('Ford', 'Model T', 2),
        ('Ford', 'Fiesta', 143),
        ('Honda', 'CR-X', 10),
        ('Honda', 'ZX', 2)
        ]
    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', cars)
