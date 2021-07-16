# List - another datatype []
# List can store multiple items in a single variable
# A list can contain same datatype values or different data type values

def calculate_square(num):
    return num * num


user_input = [10, 20, 30, 40]
print(type(user_input))
user_output = []
for list_element in user_input:  # example of for each loop
    user_output.append(calculate_square(list_element))

print(user_output)
