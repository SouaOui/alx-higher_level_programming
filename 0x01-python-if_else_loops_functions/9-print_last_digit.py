#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number *= -1
        last_digit = number % 10
        last_digit *= -1
    else:
        last_digit = number % 10
    return last_digit
