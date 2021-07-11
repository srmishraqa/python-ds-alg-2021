"""
Instead of adding a variable we can store user input as a param and pass to function to execute some task
"""


def func_calc_units(no_of_days, conversion_unit, unit_of_measurement):
    print(f"{no_of_days} days consists of {no_of_days * conversion_unit} {unit_of_measurement}")


# input() always treated as String, we need use int() to convert it to integer
input_var = int(input("Enter the no of days : \n"))  # this is user input will prompt in next line to enter user input
# we did casting here , converted String to Integer

func_calc_units(input_var, 24, "hours")
