#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = number % 10
if number < 0:
    ldigit = ((-1 * number) % 10) * -1
    if int(ldigit) > 5:
    print("Last digit of {:d} is {:d}".format(number, ldigit), end=" ")
    print("and is greater than 5")
elif int(ldigit) == 0:
    print("Last digit of {:d} is {:d}".format(number, ldigit), end=" ")
    print("and is 0")
elif int(ldigit) < 6:
    print("Last digit of {:d} is {:d}".format(number, ldigit), end=" ")
    print("and is less than 6 and not 0")
