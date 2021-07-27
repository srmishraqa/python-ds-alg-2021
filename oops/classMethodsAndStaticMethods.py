from classAndObj import Employee
import datetime

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

employee_4 = Employee.from_string('john-Ham-55000')
print(employee_4.__dict__)
print(Employee.num_of_employee)

print(employee_1.__dict__)

# this will get reassigned and that will treated as a new Object
# and the employee_1 originally constructed is an abandoned object now
employee_1 = Employee('Nazmul', 'hossain', 6200)
print(Employee.num_of_employee)
print(employee_1.__dict__)

# fromtimestamp() is an example of alternative constructor class method

# executing static method
my_date = datetime.date(2016, 7, 10)  # sunday
print(Employee.is_working_day(my_date))
my_date = datetime.date(2016, 7, 12)  # tuesday
print(Employee.is_working_day(my_date))
