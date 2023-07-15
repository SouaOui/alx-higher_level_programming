#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        result = []
        counter = 0
        for x in my_list_1:
            for y in my_list_2:
                result[counter] = x / y
                counter += 1
        return result
    except ZeroDivisionError:
        
        result[counter] = 0
        counter += 1
        