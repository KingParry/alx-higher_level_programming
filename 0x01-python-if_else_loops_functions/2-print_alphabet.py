#!/usr/bin/python3
"""program that prints the ASCII alphabet, in lowercase, not followed by a new line."""

for letty in range(97, 123):
    print("{}".format(chr(letty)), end="")
