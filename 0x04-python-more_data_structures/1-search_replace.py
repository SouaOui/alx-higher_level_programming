#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = my_list.copy()
    for item in range(len(my_list)):
        if my_list[item] == search:
            my_list[item] = replace
    return my_list
