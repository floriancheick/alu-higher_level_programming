#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import derr
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        derr.write("Exception: {}\n".format(err))
        return False
