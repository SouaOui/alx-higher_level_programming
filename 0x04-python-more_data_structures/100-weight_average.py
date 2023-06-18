#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    if my_list == []:
        return 0
    for item in my_list:
        average += (item[1] * item[0]) / sum([x[1] for x in my_list])
    return average
