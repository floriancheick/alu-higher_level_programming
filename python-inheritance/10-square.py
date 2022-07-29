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
