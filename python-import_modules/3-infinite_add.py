#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    res = 0
    len_args = len(sys.argv) - 1
    for i in range(0, len_args):
        res += int(sys.argv[i + 1])
    print("{}".format(res))
