import traceback  # imported traceback to get the exact error


def calc_value(no_of_days, conversion_unit, unit_of_measurement):
    print(f"{no_of_days} days consists of {int(no_of_days) * conversion_unit} {unit_of_measurement}")


# Try block will execute first , anywhere it runs into error, it will jump to except block
# once the error is handled it will execute the lines inside except block or else pre-mature termination of program

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
        traceback.print_exc()  # printing the stack trace
        print("The number you have entered is not a number , pls retry")


user_input = input("Enter a number --> \n")
validate_and_execute()
