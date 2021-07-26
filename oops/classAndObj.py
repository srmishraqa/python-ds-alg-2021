# class will be blueprint and Objects are instances of class
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

    def return_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    # regular method in a class automatically takes instance as first argument
    # _self_ points to instance as first argument

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

    def apply_raise(self):
        # if we apply Employee.raise_amount -> will take the class attribute value
        # if we apply self -> it will take instance variable value for that particular instance
        # if instance is not defined -> then will pick class variable value
        self.pay = self.pay * self.raise_amount
