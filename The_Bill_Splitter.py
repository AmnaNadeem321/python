# Write a program that asks the user for the total restaurant bill amount, the tip percentage they want to leave, and the
# number of people splitting the bill. Calculate the total tip, the total bill including the tip, and how much each person
# has to pay. print the results clearly.

Bill = int(input("enter your total bill: "))
Tip_per = int(input("enter your tip percentage you want to leave: "))
people = int(input("enter your number of people in group: "))

Tip= (Bill * Tip_per)/100
print("total bill is equal to", Bill + Tip)
Total_Bill = Bill + Tip
print("amount per person is equal to ", Total_Bill /people )