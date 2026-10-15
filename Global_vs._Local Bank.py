# Question 5: Global vs. Local Bank
# Define a global variable bank_balance = 5000 . Write two functions: deposit(amount) and 
# withdraw(amount) .
# Inside these functions, use the global keyword to update the bank_balance using assignment 
# operators ( += , -
# = ). Ensure that a user cannot withdraw more than their current balance. Call both functions
# and print the updated
# balance.

bank_balance = 5000

def deposit(amount):
    global bank_balance
    bank_balance += amount
    print("deposited:", amount)
    print("updated balance:", bank_balance)


def withdraw(amount):
    global bank_balance

    if amount <= bank_balance:
        bank_balance -= amount
        print("withdrawn:", amount)
        print("updated balance:", bank_balance)
    else:
        print("insufficient balance!")

deposit_amount = int(input("Enter amount to deposit: "))
deposit(deposit_amount)

withdraw_amount = int(input("Enter amount to withdraw: "))
withdraw(withdraw_amount)

print("finall bank balance:", bank_balance)
