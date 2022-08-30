#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for digit in my_list[::-1]:
        print("{:d}".format(digit))
    if not my_list:
        return None
