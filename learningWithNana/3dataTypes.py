"""
Variables are containers which hold values
datatype defining is not required , just name is required
naming convention -> all smalls separated by -> my_first_variable
reserved keywords can't be used as variable
for variable use descriptive names
"""

covert_to_units = 24 * 60 * 60
name_of_the_unit = "seconds"

print(f"20 days have {20 * covert_to_units} {name_of_the_unit}")
print(f"30 days have {30 * covert_to_units} {name_of_the_unit}")
print(f"40 days have {40 * covert_to_units} {name_of_the_unit}")
print(f"70 days have {70 * covert_to_units} {name_of_the_unit}")

first_var = "First Var"
second_var = 30.98
third_var = 10000
fourth_var = True

print(type(first_var))
print(type(second_var))
print(type(third_var))
print(type(fourth_var))
