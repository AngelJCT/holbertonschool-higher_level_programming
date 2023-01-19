#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0  # Initialize add to 0
    args_len = len(sys.argv)  # Get the length of the arguments
    for i in range(1, args_len):  # Loop through the arguments
        add += int(sys.argv[i])  # Add the arguments to add
    print("{:d}".format(add))  # Print the sum of the arguments
