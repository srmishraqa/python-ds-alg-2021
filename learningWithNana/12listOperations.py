# list always uses [] symbol
month_values = ["Jan", "Feb", "March"]

# list is always index based , the index starts with zero, to access first element we should use [0]
# accessing values from the list
print(month_values[0])
print(month_values[1])
print(month_values[2])

# add new values to the existing list
month_values.append("April")
print(month_values)

#  index which does not exist
#  print(month_values[5])
#  will give -> IndexError: list index out of range

# remove()
month_values.remove("March")
print(month_values)

#  remove() will always delete the first occurrence of the element

month_values.append("Jan")
month_values.append("Jan")
print(month_values)
month_values.remove("Jan")
print(month_values)

# length of the list
print(month_values.__len__())
