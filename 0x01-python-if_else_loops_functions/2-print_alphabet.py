#!/usr/bin/python3
import random
namb = random.randint(-10000, 10000)
digit = abs(namb) % 10
if namb < 0:
    digit = -digit
print(f"Last digit of {namb:d} is {digit:d} and is ", end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
