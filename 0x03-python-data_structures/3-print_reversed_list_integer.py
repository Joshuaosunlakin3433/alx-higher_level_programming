#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for digit in reversed(my_list):
        print("{:d}".format(digit))
    if not my_list:
        return None
