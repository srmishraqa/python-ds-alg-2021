"""data type is of 2 types text and number
Single and double quotes both works for String
for Numbers we have different data type
Integer - for whole numbers without decimal points including negative numbers
float - for decimal number
boolean - for True or False
"""
print(20 * 24 * 60)

# string concatenation
# can't concatenate numbers with string , we need to use str()
# str() -> converts everything inside the block to string
print("20 days have " + str(20 * 24 * 60) + " minutes")

# better syntax like backtick in JS using f{} in between quotes -> this works in latest python version (>3.6)
# f stands for format
print(f"20 days have {20 * 24.0 * 60} minutes")
print(True)
