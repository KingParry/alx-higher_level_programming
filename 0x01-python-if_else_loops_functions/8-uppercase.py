#!/usr/bin/python3
# creater - EP

def uppercase(str):
    """a function that prints a string in uppercase followed by a new line."""
    for g in str:
        if ord(g) >= 97 and ord(g) <= 122:
            g = chr(ord(g) - 32)
        print("{}".format(g), end="")
    print("")
