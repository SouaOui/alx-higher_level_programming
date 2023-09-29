#!/usr/bin/python3
""" implement find_peak """


def find_peak(list_of_integers):
    """find_peak

    Args:
        list_of_integers (list): list of integers

    Returns:
        integer: the peak of the given list
    """
    if len(list_of_integers) == 0:
        return None
    peak = list_of_integers[0]
    for ele in list_of_integers:
        if ele > peak:
            peak = ele
    return peak
