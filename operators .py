x = 15
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

# Addition of two numbers
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("sum is ", num1 + num2)

# subtraction of two numbers
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("sub is ", num1 - num2)

# multiplication of two numbers
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("mul is ", num1 * num2)

# division of two numbers
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("div is ", num1 / num2)

# remainder of two numbers
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
if num2 == 0: 
    print("you cannot divide a number by zero")
else:
    print("modulus is ", num1 % num2)

#square of two numbers
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("square is ", num1 * num2)

#average of two numbers
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("average of two numbers are ", (num1 + num2)/2)

#percentage calculator
total_marks = int(input("enter first number: "))
obtained_marks = int(input("enter second number: "))

percentage = (obtained_marks / total_marks) * 100
print(percentage)

#temperature convertor
celsius = int(input("enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

#assignment operator
num3 = 5
num3 += 10
print(num3)
num3 *= 2
print(num3)

#logical operator
marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("grade A+")
elif marks >= 80 and marks <= 89:
    print("grade A")
elif marks >= 70 and marks <= 79:
    print("grade B")
elif marks >= 60 and marks <= 69:
    print("grade C")
elif marks >= 50 and marks <= 59:
    print("grade D")        
elif marks < 50 :
    print("Fail") 

x = 10

def my_function():
    print(x)

my_function()

    
