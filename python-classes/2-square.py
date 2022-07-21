#!/usr/bin/python3
'''
Class Square is define in thids module
'''
class Square:
    '''
class assigns the size of square
'''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size  < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
