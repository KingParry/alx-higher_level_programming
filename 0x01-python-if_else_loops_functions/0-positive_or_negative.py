#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(s"{number:d} is positive")
elif number == 0:
    print(s"{number:d} is zero")
else:
    print(s"{number:d} is negative")
