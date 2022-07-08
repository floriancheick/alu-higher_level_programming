#!/usr/bin/python3
letter = -32
def uppercase(le):
    i = 0
    while i < len(le):
        i = i + 1
        print("")
        def islower(la):
            value = ord(la)
            if value >= 97 and value <= 122:
                return True
            else:
                return False
