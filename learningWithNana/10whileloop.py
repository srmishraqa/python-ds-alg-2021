# While loop is used for executing program multiple times till the condition becomes false
# conditions are always boolean

def calc_value(no_of_days, conversion_unit, unit_of_measurement):
    print(f"{no_of_days} days consists of {int(no_of_days) * conversion_unit} {unit_of_measurement}")


def validate_and_execute():
    try:
        user_input_int = int(user_input)
        if user_input_int > 0:
            calc_value(user_input_int, 24, "hours")
        elif user_input_int == 0:
            print("You entered a 0 , pls enter valid number")
        else:
            print("You have entered a negative number, pls retry")
    except ValueError:
        print("The number you have entered is not a number , pls retry")


user_input = ""
while user_input.lower() != "exit":
    user_input = input("Enter a number --> \n")
    validate_and_execute()
