import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("UPDATE inventory SET Model = 'Civic' WHERE Model='ZX'")
    c.execute("UPDATE inventory SET quantity = 3 WHERE Model='Bronco'")
    c.execute("SELECT * from inventory")
    for make, model, q in c.fetchall():
        print(f'{make} - {model}: {q}')
