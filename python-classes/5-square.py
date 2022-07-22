#!/usr/bin/python3
"""This module define class square."""
class Square:
    """Present a square."""
    def __init__(self, size=0):
        """new square
Args: size (int): size of new square.
"""
        self.size = size
        @property
        def size(self):
            """set current size of the square."""
            return (self.__size)
        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value <0:
                raise ValueError("size must be >= 0")
            self.__size = value
            def area(self):
                """Return current square area."""
                return(self.__size * self.__size)
