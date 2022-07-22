#!/usr/bin/python3
"""
This module define a class Square 
"""
class Square
"""
Args:size(int) 
"""
def __init__(self, size=0):
    """
Attributes:__size(int)
"""
    if type(size) is not int:
        raise  TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = size
