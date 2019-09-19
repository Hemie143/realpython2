import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("DROP TABLE orders")
    c.execute("CREATE TABLE orders (Make TEXT, Model TEXT, order_date TEXT)")

    orders = [
        ('Ford', 'Bronco', '2019-09-19'),
        ('Ford', 'Bronco', '2019-08-24'),
        ('Ford', 'Bronco', '2019-09-01'),
        ('Ford', 'Model T', '2019-09-01'),
        ('Ford', 'Model T', '2019-08-01'),
        ('Ford', 'Model T', '2019-07-01'),
        ('Ford', 'Fiesta', '2019-07-02'),
        ('Ford', 'Fiesta', '2019-07-03'),
        ('Ford', 'Fiesta', '2019-07-04'),
        ('Honda', 'CR-X', '2019-09-18'),
        ('Honda', 'CR-X', '2019-09-08'),
        ('Honda', 'CR-X', '2019-09-16'),
        ('Honda', 'Civic', '2019-09-17'),
        ('Honda', 'Civic', '2019-09-15'),
        ('Honda', 'Civic', '2019-09-05'),
        ]
    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)

    c.execute("""SELECT inventory.Make, inventory.Model, inventory.quantity,
                orders.order_date FROM inventory, orders
                WHERE inventory.Make=orders.Make AND inventory.Model=orders.Model""")
    for make, model, quantity, date in c.fetchall():
        print(f'Make: {make}')
        print(f'Model: {model}')
        print(f'Quantity: {quantity}')
        print(f'Order date: {date}')
        print()
