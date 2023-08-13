#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    result = 0
    argc = len(argv)
    if argc > 1:
        for i in range(1, argc):
            result = result + int(argv[i])
    print("{}".format(result))
