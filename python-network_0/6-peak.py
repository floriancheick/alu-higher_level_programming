#!/usr/bin/python3
"""
This function finds a peak in a list of unsorted
integers using binary sort
"""


def find_peak(list_of_integers):
    """
    function to find peak
    """
    le = len(list_of_integers)
    if le == 0:
        return
    half = le // 2
    if (half == le - 1 or list_of_integers[half] >=
        list_of_integers[half + 1]) and (half == 0 or list_of_integers[half] >=
                                         list_of_integers[half - 1]):
        return (list_of_integers[half])
    elif half != le - 1 and list_of_integers[half + 1] > list_of_integers[half]:
        return (find_peak(list_of_integers[half + 1:]))
    return (find_peak(list_of_integers[:half]))
