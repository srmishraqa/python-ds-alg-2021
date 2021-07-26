"""
The exercise is to accept user input of a goal and its deadline
and print out how much time remaining currently from the deadline
So we'll be using python built in modules datetime
"""
from datetime import datetime

#  enter the deadline - dd.mm.yyyy
user_input = input("Enter a goal with the deadline separated by colon \n")
input_list = user_input.split(":")
print(input_list)

goal = input_list[0]
deadline = input_list[1].strip()  # deadline is already in string , we need to convert into datetime format

# we will use datetime module's datetime class' strptime()
# we need to define the format in 2nd param to define the date format input
print(datetime.strptime(deadline, "%d.%m.%Y"))
print(type(datetime.strptime(deadline, "%d.%m.%Y")))

#  calculate how many days now to deadline
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
current_date = datetime.today()
print(current_date)
time_remaining = deadline_date - current_date
print(time_remaining)
print(f"Dear User ! Time remaining for your goal of {goal.strip()} is {time_remaining.days} days")
