"""
Functions - blocks of code that does something to give output and avoids repeating activities
Function is where re-usability happens
def used to define -> then give a name -> a descriptive name
then -> ():
"""
covert_to_units = 24 * 60
name_of_the_unit = "minutes"


#  here we have defined the function
def convert_days_to_units():
    print(f"20 days have {20 * covert_to_units} {name_of_the_unit}")
    print("All Good!!")


#  here we need to use the function by calling it
convert_days_to_units()


#  function with input parameters
def convert_days_to_units_with_params(no_of_days, unit_param, unit_name):
    print(f"{no_of_days} days have {no_of_days * unit_param} {unit_name}")
    print("All Executed!!")


convert_days_to_units_with_params(30, 24 * 60 * 60, "seconds")
