#!/usr/bin/python3
for i in range(ord('z'), ord('`'), -1):
    if i % 2 == 0:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i).upper()), end="")
