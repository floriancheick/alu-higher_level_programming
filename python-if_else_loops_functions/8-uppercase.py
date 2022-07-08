#!/usr/bin/python3
value = -32
def upppercase(str):
    i =0
    while i < len(str):
        if islower(str[i]):
            lower = ord(str[1]) + value
            new = chr(lower)
        else:
            new = str[1]
            print("{}".format(new),  end= '')
            i = i + 1
            print("")
            def islower(str):
                value1 = ord(str)
                if value1 >= 97 and value1 <= 122:
                    return True
                else:
                    return False
