#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_args = len(sys.argv) - 1
    if len_args == 1:
        print("{} argument:".format(len_args))
        print("1: {}".format(sys.argv[1]))
    elif len_args == 0:
        print("{} arguments.".format(len_args))
    else:
        print("{} arguments:".format(len_args))
        for i in range(0, len_args):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
