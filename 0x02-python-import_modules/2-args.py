#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv)
    i = 1
    if num_arg == 1:
        print("0 arguments.")
    else:
        if num_arg == 2:
            print("{:d}" .format(num_arg - 1), "argument:")
        elif num_arg > 2:
            print("{:d}" .format(num_arg - 1), "arguments:")
            while num_arg != 1:
                print("{:d}:" .format(i), sys.argv[i])
                i += 1
                num_arg -= 1
