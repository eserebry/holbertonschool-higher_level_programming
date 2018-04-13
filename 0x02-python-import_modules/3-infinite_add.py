#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv)
    i = 1
    sum_arg = 0
    if num_arg == 1:
        print("0")
    else:
        if num_arg == 2:
            print(sys.argv[i])
        else:
            while num_arg != 1:
                sum_arg += int(sys.argv[i])
                i += 1
                num_arg -= 1
            print("{:d}" .format(sum_arg))
