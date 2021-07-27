"""
Inheritance is the process - by which we can inherit the class attributes and methods form Parent class to Child class
In that way without disturbing Parent class method implementation we can override the implementation in the child class
And along with that we can add new methods and new implementation
which was not present inside the parent class into the child class
"""
from classAndObjCall import Employee


class Developer(Employee):
    raise_amount = 1.12

    # Instead of creating a complete new init method we created a init and
    # asked super class ctc to handle all the existing Params , we did call to super()
    # and we handled the new prams
    def __init__(self, first_name, last_name, pay, progrmming_lang):
        super().__init__(first_name, last_name, pay)
        self.progrmming_lang = progrmming_lang


class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('--->', emp.return_full_name())


############################
# Execution
# print(help(Developer))

dev_1 = Developer('Soumya', 'Mishra', 40000, 'Python')
dev_2 = Developer('A', 'B', 3000, 'Java')
print('---- Inherited Class Execution -----')

print(dev_1.pay)
# raise % will be applied of Developer class overridden value
dev_1.apply_raise()
print(int(dev_1.pay))

print(dev_1.progrmming_lang)
print(dev_2.progrmming_lang)

mgr_1 = Manager('SU', 'CHANG', 90000, [dev_1])

print(mgr_1.email)
print("---------------------------")
print(mgr_1.print_employees())
print("---------------------------")
mgr_1.add_employee(dev_2)

print(mgr_1.print_employees())
print("---------------------------")
mgr_1.remove_employee(dev_1)

print(mgr_1.print_employees())
print("---------------------------")

"""
inbuilt methods for Child classes
isinstance() - will tell us if an object is an instance of a class or not , returns boolean
issubclass() - will tell us if a class is a subclass of the other class or not , returns boolean
"""
print(isinstance(mgr_1, Manager))
print("---------------------------")
print(isinstance(mgr_1, Employee))
print("---------------------------")
print(isinstance(dev_1, Manager))
print("---------------------------")

print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))

# Example - HHTPException class inherits form Exception Class
