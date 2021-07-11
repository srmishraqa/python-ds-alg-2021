from math import *

print(2)
print(2.097)
print(-2.098)
print((2 * 8) / 100)
#   mod operator
print(10 % 3)

my_num = 5
print(my_num)
#  converting number into a string str()
a = str(my_num)
print(isinstance(a, str))

#  Math Functions
my_dec = -2
print(abs(my_dec))  # absolute value -> abs()
print(pow(my_num, 3))  # pow(3,2) -> 3*3 = 9
print(max(my_num, my_dec))  # max(3,2) -> returns max of two -> 3
print(min(my_num, my_dec))  # min(3,2) -> returns min of two -> 2

round_var = 3.8  # round() -> makes floating pt number as nearest round numbers
print(round(round_var))
round_var = 3.1
print(round(round_var))
round_var = 3.5
print(round(round_var))

print(floor(round_var))  # floor () -> chops off the decimal part
print(ceil(4.1))  # ceil()  -> round the number
print(round(4.1))
print(sqrt(36.0))  # sqrt() -> square root
