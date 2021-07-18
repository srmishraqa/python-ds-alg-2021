from classAndObj import Employee

print(Employee.num_of_employee)

emp1 = Employee('Soumya', 'Mishra', 5000)
emp2 = Employee('Jitendra', 'Patra', 45000)

# here we are calling the method by reference variable
# HERE THE METHOD KNOWS TO RUN WITH WHICH INSTANCE
print(emp1.return_full_name())
# in background the first call gets converted into second call

# here we are calling by class and passing the ref variable instance
# because if we don't pass instance variable the class does not know to run that method with which instance
print(Employee.return_full_name(emp2))

print(str(emp1.email).lower())
print(str(emp2.email).lower())

# this will print the namespace or object values of the emp1 Instance and if we see there is no raise amount in there
# __dict__ mean -> A dictionary or other mapping object used to store an object's (writable) attributes.
print(emp1.__dict__)

# Class Variables can be accessed by class name as well as instance name and both points to same
# when we try to access an attribute, First check is if instance contains ( constructor ) that attribute,
# if not then check if the class or the class it inherits form contains that attribute or not
print(f"the raise_amount key for Employee class is {Employee.__dict__.get('raise_amount')} and it is a class attribute")
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("___________________")

# setting class variable values on class level
Employee.raise_amount = 1.06
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("___________________")

print(emp1.__dict__)
print("___________________")
# setting class variable values at instance level
emp1.raise_amount = 1.08
print("___________________")
print(emp1.__dict__)

print("___________________")
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print('--------->')
print(Employee.num_of_employee)
print(emp1.num_of_employee)


