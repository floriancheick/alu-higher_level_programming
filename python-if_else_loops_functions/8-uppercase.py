#!/usr/bin/python3
def uppercase(str):
    le = ''
    for i in str:
        if (i >= 'a' and i <= 'z'):
            le = le + chr((ord(i) -32))
        else:
            le = le +1
            print("{}".format(le))
