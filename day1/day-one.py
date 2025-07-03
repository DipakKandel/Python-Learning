# Storing text (string)
name = "Dipak"

# Storing number (integer)
age = 25

# Storing decimal number (float)
height = 5.9

# Storing True/False (boolean)
is_student = True
print(name)
print(age)
print(height)
print(is_student)


print("Hello, world!")
print("Your name is", name)


yearOfBirth = int(input("Enter your year of birth: "))   # still a string
placeOfBirth = input("enter your birth country: ")
# yearOfBirth = int(yearOfBirth)  # now it's an integer
print(f"Hi {name} I know that you are from {placeOfBirth} Your current age is: {2025 - yearOfBirth}")