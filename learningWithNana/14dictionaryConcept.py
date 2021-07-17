"""
dictionary contains key value pairs like Map in Java
syntax:
my_dictionary = {"Jan":1,"Feb':2,"Mar":3}
"""

my_user_input = input("Enter a string \n")
print(my_user_input)
my_list = my_user_input.split(":")
print(my_list)
my_dictionary = {"no_of_units": my_list[0], "unit": my_list[1]}
print(my_dictionary)
print(type(my_dictionary))

# Will take input and convert into minutes -> like 20:minutes
if int(my_dictionary['no_of_units']) > 0:
    op = (int(my_dictionary["no_of_units"]) * 60)
    print(f"{my_dictionary['no_of_units']} hour contains {op} {my_dictionary['unit']}")
"""
Summary:
1. String - texts
2. Int - whole numbers
3. Float - decimal pt numbers
4. Boolean - to check flagged condition -> returns only true or false
5. List - list of elements containing unique or duplicate values , can be indexed
6. Set - stores unique values and can't be indexed and random ordered
7. Dictionary - stores data in form of key value pairs like Map in java
"""