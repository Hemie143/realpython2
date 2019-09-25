import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    '''
    c.execute("""SELECT inventory.Make, inventory.Model, inventory.quantity,
                orders.Make, orders.Model, COUNT(orders.order_date)
                FROM inventory, orders
                WHERE inventory.Make=orders.Make AND inventory.Model=orders.Model""")
    '''
    c.execute("""SELECT inventory.Make, inventory.Model, inventory.quantity,
                orders.Make, orders.Model, COUNT(orders.order_date)
                FROM inventory, orders
                WHERE inventory.Make=orders.Make AND inventory.Model=orders.Model
                GROUP BY orders.Model""")
    for make, model, quantity, _, _, orders in c.fetchall():
        print(f'Make: {make}')
        print(f'Model: {model}')
        print(f'Quantity: {quantity}')
        print(f'Orders: {orders}')
        print()
