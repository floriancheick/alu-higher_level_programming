#!/usr/bin/python3
def magic_string():
    magic_string_c = getattr(magic_string, 'n', 0) + 1
    return ("Holberton, " * (magic_string_c - 1) + "Holberton")
