#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv)
    result = 0
    for item in range(1, argv_len):
        result += int(argv[item])
    print(result)
