"""
Any Plain text can be stored inside strings - use "" marks for strings
"""
print("Giraffe Academy")

print("Giraffe \nAcademy")  # \n creates a new line

print("Giraffe \"Academy")  # \ used for escape sequence

print_phrase = "Khan Academy"
print(print_phrase)  # printing a variable

# concatenation
print(print_phrase + " is cool....")

#  functions -->
print(print_phrase.lower())  # lower() converts to lower case
print(print_phrase.upper())  # upper() converts string to upper case
print(print_phrase.isupper())  # isupper() - returns true if the string is in upper case
print(print_phrase.islower())  # islower() - returns true if the string is in lower case
print(print_phrase.upper().isupper())

#  string length -> len()
print(len(print_phrase))

#  grab the 1st character - index 0
print(print_phrase[0].lower())
print(print_phrase[11])
#  print(print_phrase[12]) - IndexError: string index out of range
# index() -> returns 1st index
print(print_phrase.index("a"))
print(print_phrase.index("Academy"))
#  print(print_phrase.index("academy")) -> ValueError: substring not found
#  replace
print(print_phrase.replace("Khan", "Mishra"))
