#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        while x > 0:
            print("{}".format(my_list[counter]), end="")
            counter += 1
            x -= 1
        print("")
    except IndexError:
        print("")
    except Exception:
        print("other errors")
    return counter
