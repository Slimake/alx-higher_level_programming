#!/usr/bin/python3
for i in range(ord('z'), ord('`'), -1):
    if i % 2 == 0:
        print("{:c}".format(chr(i)), end="")
    else:
        print("{:c}".format(chr(i).upper()), end="")
