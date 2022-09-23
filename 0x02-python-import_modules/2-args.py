#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument_no = len(sys.argv) - 1
    if argument_no == 0:
        print("{:d} arguments.".format(argument_no))
    elif argument_no == 1:
        print("{:d} argument".format(argument_no))
        print("{:d}: {}".format(argument_no, (sys.argv)[1]))
    else:
        print("{:d} arguments.".format(argument_no))
        for i in range(1, argument_no + 1):
            print("{:d}: {}".format(i, (sys.argv)[i]))
