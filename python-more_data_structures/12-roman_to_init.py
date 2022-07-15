#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is not str) or roman_string is None:
        return 0
    if type(roman_string) is str:
        le = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        li = 0
        for x, y in zip(roman_string, roman_string[1:]):
            if x not in le.keys():
                return 0
            elif le[x] >= le[y]:
                li += le[x]
            else:
                li -= le[x]
        li += le[roman_string[-1]]
        return li
