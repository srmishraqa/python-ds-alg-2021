"""
Variable scope means - where is the variable the function usage defined
Outside function - global scope - accessible to all function
Variables created with in the function used inside only - local/internal scope
"""

my_variable = 10  # global var


def test_function(test_var):  # local var
    print(my_variable)
    print(test_var)


def test_scope():
    print(my_variable)
    # print(test_var) # local variable can't be accessed with in another function
