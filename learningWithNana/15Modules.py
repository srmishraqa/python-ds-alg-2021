"""
Module is basically a python file which contains functions and variables which can be used by other python files
"""
# import moduleHelper
# here we have imported other file where we have written a function

# this import will entirely import the file
# if we want to import only a specific function -- we need to to follow the below syntax
from moduleHelper import return_reverse_num, user_input_var

# import moduleHelper as m_helper

# Now all the variables and functions of moduleHelper.py file is available to this .py file

input_number = input("Enter a number \n")
if input_number.isdigit():
    if int(input_number) > 0:
        # we are using the function of imported file and calling that function by using file name and . operator if
        # entire file is imported . we can directly call the function if we have imported that , no need to write file
        # name and call it by dot operator
        if return_reverse_num(int(input_number)) == int(input_number):
            print(f"Number {input_number} is palindromic")
        else:
            print(f"Number {input_number} is non-palindromic")
else:
    print(f"{input_number} is not a valid number")

print("successfully executed")
print(f"The enter input is {user_input_var}")

# python has inbuilt modules as well
