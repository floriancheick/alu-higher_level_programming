#!/usr/bin/python3
def divisible_by_2(my_list=[]):
        if my_list:
                list_one = []
                for i in my_list:
                        if 1 % 2 == 0:
                                list_one.append(True)
                        else:
                                list_one.append(False)
                                return list_one
