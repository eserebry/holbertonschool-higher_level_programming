#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    num_arg = len(sys.argv)
    if num_arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] != "+" and sys.argv[2] != "-"\
       and sys.argv[2] != "/" and sys.argv[2] != "*":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{:d} + {:d} = {:d}" .format(a, b, add(a, b)))
        if sys.argv[2] == "-":
            print("{:d} - {:d} = {:d}" .format(a, b, sub(a, b)))
        if sys.argv[2] == "*":
            print("{:d} * {:d} = {:d}" .format(a, b, mul(a, b)))
        if sys.argv[2] == "/":
            print("{:d} / {:d} = {:d}" .format(a, b, div(a, b)))
