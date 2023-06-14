#!/usr/bin/python3
def weight_average(my_list):
    if not my_list:
        return 0

    sum_product = 0
    total_weight = 0

    for score, weight in my_list:
        sum_product += score * weight
        total_weight += weight

    return sum_product / total_weight
