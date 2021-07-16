"""
split() converts string to list based on spaces or comma or any parameter
input = '10 20 30 40'
output = [10,20,30,40]
here input datatype is String
and output datatype is list containing string elements
"""
user_ip = input("Enter a String to split \n")
print(type(user_ip))
user_op = user_ip.split(", ")
print(user_op)
print(type(user_op))

for elements in user_op:
    print(type(elements))

for elements in user_op:
    print(int(elements) * int(elements))
