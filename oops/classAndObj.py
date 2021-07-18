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

    def apply_raise(self):
        # if we apply Employee.raise_amount -> will take the class attribute value
        # if we apply self -> it will take instance variable value for that particular instance
        # if instance is not defined -> then will pick class variable value
        self.pay = self.pay * self.raise_amount
