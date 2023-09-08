#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    total = 0
    for i in sys.argv:
        if sys.argv.index(i) > 0:
            total += int(i)
    print("{:d}".format(total))
