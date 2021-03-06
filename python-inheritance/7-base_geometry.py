#!/usr/bin/python3
"""This module contains class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
