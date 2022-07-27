#!/usr/bin/python3
"""This module inherits from BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """class BaseGeometry"""

    def __init__(self, width, height):
        """initialization"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
