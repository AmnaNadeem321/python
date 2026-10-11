#while loop
i = 1
while i <= 20:
    print(i)
    i+= 1

print("loop ended")

#table of 5
i = 5
n = 1
while n<=10:
    print(i*n)
    n += 1
print("loop ended")


#suqares of number 
i = 1
n = 1
while n<=10:
    print(i*n)
    n += 1
    i += 1
print("loop ended")

#for loop

fruits = ["apple", "banana" , "cherry", "pineapple"]
for x in fruits:
    print(x)

#use of break statement
i = 1
while i < 9:
    print(i)
    if i == 3:
        break
    i+=1

#continue statement
#Skip the iteration and continue with the next iteration
i = 0
while i < 9:
    i+=1
    if i == 5:
        continue
    print(i)
  
