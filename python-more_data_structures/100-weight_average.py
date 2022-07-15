#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        le = 0
        li = 0
        for tup in my_list:
            scores, weight = tup
            le += scores * weight
            li += weight
        return (sums / dvd) if dvd > 0 else 0
    else:
        return 0
