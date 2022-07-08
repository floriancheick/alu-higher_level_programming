#!/usr/bin/python3
def uppercase(str)
uppercase = ''
for i in str:
    if (i >= 'a' and i <= 'z'):
        uppercase = uppercase + chr((ord(i) -32))
    else:
        uppercase = uppercase + 1
        print("{}".format(uppercase))
