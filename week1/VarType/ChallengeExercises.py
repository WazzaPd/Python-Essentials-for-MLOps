# Create a script that adds two numeric user inputs and prints output
result = 1 + 2
print(result)

# Use f-strings and input variables to print a customized greeting
name = "Joseph Wu"

print(f"Hi, my name is {name}")

# Catch a ZeroDivision Error to print a user-friendly error message
try:
    result = 14/0
    print(result)
except ZeroDivisionError as error:
    print(f"There was an error: {error}")

# Cause and handle a TypeError by concatenating the wrong data types
try:
    result += "50"
except TypeError as error:
    result += 50
print(result)

# Write exception handling that differentiates multiple errors
try:
    #result = 14/0
    result += "50"
except (ZeroDivisionError, TypeError) as error:
    print(f"There was an error: {error}")