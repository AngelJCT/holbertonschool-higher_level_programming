#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv
    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    arg_operator = argv[2][0]
    b = int(argv[3])

    if arg_operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif arg_operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif arg_operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif arg_operator == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
