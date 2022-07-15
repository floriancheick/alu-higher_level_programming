#!/usr/bin/python3
def divisible_by_2(my_list=[]):
        list_num = []
        for list_one in my_list:
            if list_one % 2 == 0:
                list_one.append(True)
            else:
                list_one.append(False)
                return list_one

