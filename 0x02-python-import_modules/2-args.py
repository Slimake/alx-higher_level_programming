#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args_len = len(argv)
    if args_len == 1:
        print("{} arguments.".format(args_len - 1))
    elif args_len == 2:
        print("{} argument:".format(args_len - 1))
    else:
        print("{} arguments:".format(args_len - 1))

    for i in range(1, args_len):
        print("{}: {}".format(i, argv[i]))
