#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0 or idx > len(my_list) - 1):
        cpy_list = my_list.copy()
        return (cpy_list)
    else:
        for i in range(len(my_list)):
            cpy_list = my_list.copy()
            cpy_list[idx] = element
            return (cpy_list)
