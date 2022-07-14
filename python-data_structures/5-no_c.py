#!/usr/bin/python3
def no_c(my_str):
    my_str = ''
    for i in range (len(my_str)):
        if my_str[i] == 'C' or my_str[i] == 'c' :
            continue
        my_str_cp = my_str_cp + my_str[i]
        my_str = my_str_cp
        return my_str
