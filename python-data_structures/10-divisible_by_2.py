#!/usr/bin/python3
def divisible_by_2(my_list=[]):
        list_one = []
        for i in range(len(my_list)):
                if my_list[i] % 2 == 0:
                        list_one.append(True)
                else:
                        list_one.append(False)
                return(list_one)
