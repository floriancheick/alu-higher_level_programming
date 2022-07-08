#!/usr/bin/python3
def uppercase(str):
    for le in str:
        if ord(letter) >= 97 and ord(le) <= 123:
            la = chr(ord(letter) - 32)
            le = la
            print("{}".format(le), end='')
            print()
