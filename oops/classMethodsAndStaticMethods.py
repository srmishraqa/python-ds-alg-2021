from classAndObj import Employee

print(Employee.num_of_employee)

employee_1 = Employee("Sarat", "Chandra", 69000)
employee_2 = Employee("Bankim", "Raman", 71000)

print(Employee.num_of_employee)

print(employee_1.__dict__)
print(employee_2.__dict__)

print(Employee.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)

Employee.set_raise_amount(1.07)

print(Employee.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)

# we can run class methods by instance reference as well

employee_2.set_raise_amount(1.09)

print(Employee.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)

# creating an Instance using alternative constructor
employee_3 = Employee.from_string('john-doe-45000')

print(Employee.num_of_employee)
print(employee_3.__dict__)
