#!/usr/bin/python3
def no_c(my_string):
    my_str = ''
    for i in range (len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c' :
            continue
        my_str = my_str + my_string[i]
        my_string = my_str
        return my_string
