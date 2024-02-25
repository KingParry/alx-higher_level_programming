#!/usr/bin/python3
for s in range(0, 10):
    for t in range(0, 10):
        if s != t and s < t:
            print("{:d}{:d}".format(s, t), end="")
            if s == 8 and t == 9:
                print("")
            else:
                print(", ", end=""))
