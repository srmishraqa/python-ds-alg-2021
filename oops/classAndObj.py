# class will be blueprint and Objects are instances of class
import datetime


class Employee:
    raise_amount = 1.04
    num_of_employee = 0

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@gmail.com'
        Employee.num_of_employee += 1  # it will increment the employee count everytime we create an Obj
        # and it will constant for all objects and not instance specific

    # since self is added automatically , this type method is called instance methods
    def return_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    # regular method in a class automatically takes instance as first argument
    # _self_ points to instance as first argument

    def apply_raise(self):
        # if we apply Employee.raise_amount -> will take the class attribute value
        # if we apply self -> it will take instance variable value for that particular instance
        # if instance is not defined -> then will pick class variable value
        self.pay = self.pay * self.raise_amount

    # repr() - magic method
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first_name, self.last_name, self.pay)

    # str() - magic method
    def __str__(self):
        return '{} - {}'.format(self.return_full_name(), self.email)

    # add() - magic method
    def __add__(self, other):
        return self.pay + other.pay

    # len() - to get the length of the employee's full name
    def __len__(self):
        return len(self.return_full_name())

    # All these magic functions called Dunder methods
    """
    To turn a regular method into a class method
    we need to add a decorator called @classmethod
    """

    # instead of self we will use cls for class method
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Alternative Constructor using class method
    # we will pass a string like -> firstName-lastName-pay
    # and will create an alternative constructor class method out of this

    @classmethod
    def from_string(cls, input_string):
        first_name, last_name, pay = input_string.split('-')
        return cls(first_name, last_name, pay)

    """
    Static methods does not add anything as argument , neither cls nor self
    They behave like normal functions and but since we put it in a class as it has some logical connections
    static method has a decorator called @staticmethod
    A method can be declared as static method if we don't access the instance or the class anywhere with in the function
    This static method is getting executed in classMethodsAndStaticMethods.py
    """

    @staticmethod
    # we are taking a day as input and returning as whether working day or not
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


"""
Special or Magic Methods
__repr__  -> unambiguous representation of object / for debugging
__str__   -> represents a readable Object and used for display
if we call str() and it is not defined repr() is the fallback option
Always good to define repr() and then go for str()
"""

# ------------------calling magic functions------------------

emp_11 = Employee("chota", "rajan", 100000)
emp_12 = Employee("Bada", "Chote", 98000)

print(repr(emp_11))
print(str(emp_12))
print(emp_11)

print(emp_11+emp_12)
print(emp_12.__len__())
