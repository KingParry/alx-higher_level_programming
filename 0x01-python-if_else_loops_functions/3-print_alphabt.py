#!/usr/bin/python3
for letty in range(97, 123):
    if chr(letty) == 'q' and chr(letty) == 'e':
        continue
    else:
        print("{}".format(chr(letty)), end="")
