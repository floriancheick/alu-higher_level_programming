#!/usr/bin/python3
def divisible_by_2(my_list=[]):
        list_one = []
        if list_one:
                for i in my_list:
                        list_one.append(False if i % 2 else True)
                        return list_one
