"""
This file will be modularized and can be accessed by other files
"""


def return_reverse_num(num):
    num_output = 0
    while num != 0:
        remainder = num % 10
        num_output = int(num_output * 10) + remainder
        num = int(num / 10)
    return num_output


user_input_var = input("Enter something \n")
