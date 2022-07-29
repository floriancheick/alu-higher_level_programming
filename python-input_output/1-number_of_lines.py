#!/usr/bin/python3
"""This module define a text file line-counting function."""


def number_of_lines(filename=""):
    """This return the number of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            line += 1
            return lines
