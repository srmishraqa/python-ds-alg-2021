def return_reverse_num(num):
    num_output = 0
    while num != 0:
        remainder = num % 10
        num_output = int(num_output * 10) + remainder
        num = int(num / 10)
    return num_output


input_number = input("Enter a number \n")
if input_number.isdigit():
    if int(input_number) > 0:
        if return_reverse_num(int(input_number)) == int(input_number):
            print(f"Number {input_number} is palindromic")
        else:
            print(f"Number {input_number} is non-palindromic")
else:
    print(f"{input_number} is not a valid number")

print("successfully executed")
