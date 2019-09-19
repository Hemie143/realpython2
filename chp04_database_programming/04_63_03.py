import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("SELECT * from inventory WHERE Make = 'Ford'")
    for make, model, q in c.fetchall():
        print(f'{make} - {model}: {q}')
