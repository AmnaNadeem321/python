# Create a number guessing game. Set a secret number (e.g., 42). Allow the user a maximum of 5
# attempts to guess it
# using a while loop.
# If they enter a number less than 1 or greater than 100, use continue to skip the attempt
# without counting it.
# If they guess correctly, print a success message and break the loop.
# Use the else block with the while loop to print "Game Over! You lost." if they run out of attempts.

secret_number = 82
n = 0
while n < 5:
    number = int(input("enter any number: "))
    if number < 1 or number > 100:
        continue
    n +=1
    if number == secret_number:
        print("WOW you guess it right")
        break
    else:
        print("wrong attempt")
else:
    print("game over you lost")        



