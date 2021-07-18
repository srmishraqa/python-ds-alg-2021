"""
We need a blueprint to define properties and behavior
to have uniformity and re-usability
The blueprint is called class
The specific implementation is called Object
Class - blueprint of the building
Object - A single building made out of the blueprint
"""


class User:  # class should be starting with caps and all classes should have __init__ function
    # this init function called is constructor
    # self is the reference to the current instance of class
    # it is used to access the variables of the same class
    # variables also needs to be defined using self keyword
    # all those params defined inside constructor must be provided
    # while creating Object of the class and needs to be assigned

    # init ctc to set class attributes whenever we create object of the class
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    # we need to pass self as a param for functions as well
    # we can do those functions on the constructed Object
    # functions belonging to a class called methods
    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_title):
        self.current_job_title = new_title

    def get_user_info(self):
        print(f"Name of the user is {self.name}")
        print(f"Email id of the user is {self.email}")
        print(f"Job Title of the user is {self.current_job_title}")

# This file will be only used for class definition
