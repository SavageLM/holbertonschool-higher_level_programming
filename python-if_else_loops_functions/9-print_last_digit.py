#!/usr/bin/python3
def print_last_digit(number):

    digit = abs(number) % 10
    if number < 0:
        digit = digt * -1
    print("{:d}".format(digit))
    return digit