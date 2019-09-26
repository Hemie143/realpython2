import pdb
import sys
from random import choice

random1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while True:
    print("To exit this game, type 'exit'")

    pdb.set_trace()

    answer = input("What is {} times {}?".format(choice(random2), choice(random1)))

    if answer == "exit":
        print("Now exiting game!")
        sys.exit()
    elif answer == choice(random2) * choice(random1):
        print("Correct!")
    else:
        print("Wrong!")
