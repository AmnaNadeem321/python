# String Slicer & Manipulator
# Write a program that takes a user's full name as input (e.g., "Muhammad Ali"). Use string
#  slicing and indexing to
# extract the first name and the last name into separate variables. Print the following:
# The initials (e.g., "M. A.").
# The entire name in uppercase.
# The entire name reversed.


full_name = input("enter your full name: ")

#for getting first name 
space = full_name.index(" ")

first_name = full_name[:space]
last_name = full_name[space + 1:]

print("initials are :", first_name[0] +  last_name[0])

#name in uppercase 
print("Uppercase:", full_name.upper())

#name in reverse
print("Reversed name:", full_name[::-1])
