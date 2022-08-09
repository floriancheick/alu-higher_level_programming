#!/usr/bin/python3
"""
Module 5-text_indentation.py
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    newtxt = text.split('\n')
    for line in newtxt:
        product = line.strip(' ')
        print(product)
