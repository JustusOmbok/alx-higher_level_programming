#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()

    for num in my_list:
        unique_set.add(num)

    total = sum(unique_set)

    return total
