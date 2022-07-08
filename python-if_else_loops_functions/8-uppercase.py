#!/usr/bin/python3
def uppercase(str):
    upcase = ''
    for i in str:
        if (i >= 'a' and i <= 'z'):
            upcase = upcase + chr((ord(i) - 32))
        else:
            upcase = upcase + 1
            print("{}".format(upcase))
