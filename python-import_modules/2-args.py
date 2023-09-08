#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("{:d} argument:".format(len(sys.argv) - 1))
else:
    print("{:d} arguments:".format(len(sys.argv) - 1))
for i in sys.argv:
    if sys.argv.index(i) > 0:
        print("{:d}: {:s}".format(sys.argv.index(i), i))
