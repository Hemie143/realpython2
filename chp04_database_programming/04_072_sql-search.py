import sqlite3

prompt = '''
Select the operation you want to perform (1-5):
1. Average
2. Max
3. Min
4. Sum
5. Exit
'''

operation = {'1': 'AVG', '2': 'MAX', '3': 'MIN', '4': 'SUM'}

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    while True:
        choice = input(prompt)
        if choice in ['1', '2', '3', '4']:
            c.execute(f"SELECT {operation[choice]}(num) from numbers")
            result = c.fetchone()
            print(f'Result: {result[01]}')
        elif choice == '5':
            break
        else:
            print('Invalid choice.')
