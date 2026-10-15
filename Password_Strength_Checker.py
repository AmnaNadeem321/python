# Write a program that takes a password as input() from the user. Check the strength of the password using the
# following rules:
# Strong: At least 8 characters long, contains both uppercase and lowercase letters, and has at least one number
# (Use string functions like .isupper() , .islower() , .isdigit() ).
# Moderate: At least 6 characters long but missing either uppercase letters or numbers.
# Weak: Less than 6 characters.


password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("strong password")
elif len(password) >= 6:
    print("moderate password")
else:
    print("weak password")
