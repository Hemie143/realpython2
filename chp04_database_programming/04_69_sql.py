import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT TABLE Make, Model, count(orders) from orders")


    c.execute("""SELECT inventory.Make, inventory.Model, count(inventory.quantity),
                orders.order_date FROM inventory, orders
                WHERE inventory.Make=orders.Make AND inventory.Model=orders.Model""")
    for make, model, quantity, date in c.fetchall():
        print(f'Make: {make}')
        print(f'Model: {model}')
        print(f'Quantity: {quantity}')
        print(f'Order date: {date}')
        print()
