# set is a list of elements which are unique , set does not allow duplicate values but list allows duplicates
my_list = [10, 20, 10, 20, 30, 40, 40, 30]
print(my_list)
print(type(my_list))

# set() converts list to a set and removes duplicates as well
# set is represented by curly braces {}
my_set = set(my_list)
print(my_set)
print(type(my_set))

# create a set
my_set_2 = {'Jan', 'Feb', 'Mar', 'Apr'}
print(my_set_2)  # may or may not print in same order

"""
Sets are unordered and unchangeable
Items in the sets do not have a defined order
items can't be referenced by index
Items can't be changed , only can be added or removed
elements can be accessed in a for loop
"""
for elements in my_set_2:
    print(elements)

# add element to set
my_set_2.add("May")
print(my_set_2)

# adding duplicates - not allowed
my_set_2.add("Jan")
print(my_set_2)

# remove an element
my_set_2.remove("Feb")
print(my_set_2)
