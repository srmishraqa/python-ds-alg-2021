def func_calc_units(no_of_days, conversion_unit, unit_of_measurement):
    if no_of_days.isdigit():
        if int(no_of_days) > 0:  # comparison operator
            print(f"{no_of_days} days consists of {int(no_of_days) * conversion_unit} {unit_of_measurement}")
        elif int(no_of_days) == 0:
            print("0 is not a valid input")
    else:
        print("The entered valued is not valid , please enter a valid input")


input_value = input("Enter a number : \n")
func_calc_units(input_value, 24, "hours")


def calc_greater_number(number_1, number_2):
    condition_check = number_1 != number_2
    print(type(condition_check))
    if condition_check:
        if number_1 > number_2:
            return number_1
        else:
            return number_2
    else:
        return number_1


input_var_1 = int(input("Enter the first Number : \n"))
input_var_2 = int(input("Enter the second Number : \n"))
output_var = calc_greater_number(input_var_1, input_var_2)
print(f"the largest number is {output_var}")

# if will always have a conditional statement which always returns boolean type value
# if and elif has conditions and else does not have any condition
