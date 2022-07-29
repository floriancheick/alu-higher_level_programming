#!/usr/bin/python3
"""This module define a Rectangle subclass Square."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Rectangle"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        def area(self):
            return self.__size ** 2
        def __str__(self):
            return "[{:s}] {:d}/{:d}".format(type(self).__name__,
                                             self.__size, self.__size)
