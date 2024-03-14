#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argv_len = len(argv) - 1
    if argv_len == 0:
        print("0 arguments.")
    elif argv_len == 1:
        print("{0:d} argument:".format(argv_len))
    else:
        print("{0:d} arguments:".format(argv_len))
    for i in range(1, len(argv)):
        print("{0:d}: {1:s}".format(i, argv[i]))
