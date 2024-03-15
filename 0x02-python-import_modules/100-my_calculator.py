#!/usr/bin/python3

if __name__ == "__main__":
    """Perform arithmetic operation using input from the command line"""
    import sys
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    argv_len = len(argv) - 1

    if argv_len < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    sign = argv[2]

    if sign == "+":
        result = add(a, b)
    elif sign == "-":
        result = sub(a, b)
    elif sign == "-":
        result = mul(a, b)
    elif sign == "/":
        result = div(a, b)
    else:
        print(f"Unknown operator. "
              f"Available operators: +, -, * and /")
        exit(1)

    print("{0:d} {1:s} {2:d} = {3:d}".format(a, sign, b, result))
