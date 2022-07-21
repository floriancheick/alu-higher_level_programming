#!/usr/bin/python3
"""
This module define class square
"""
class Square:
    """
Args:size(int) -class Square definition
"""
    def __init__(self, size=0):
        self.size = size
        @property
        def size(self):
            return self.__size
        @size.setter
        def size(self, value):
            if type (value) is not init:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
                def area(self):
                    retun(self.size)**2
                    def my_print(self):
                        if self.__size !=0:
                            for row in range(self.__size):
                                print("#", end="")
                                print()
                            else:
                                print()
