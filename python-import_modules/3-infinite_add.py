#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    args_len = len(sys.argv)
    for i in range(1, args_len):
        add += int(sys.argv[i])
    print("{:d}".format(add))
