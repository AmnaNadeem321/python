#List-----mutable
list1 = [1, 2, 3, 4, 5]
print(type(list1))

print(len(list1))

list1.append(6)
print(list1)

list1.remove(1)
print(list1)

list1.pop(4)
print(list1)

#palindrome
list2 = [1, 2, 3, 2, 1]
orig = list2.copy()
orig.reverse()
print(list2)
if  orig == list2:
    print("this list is palindrome")
else:
    print("this list is not palindrome")    


#largest number in the list
list3  = [1, 2, 3, 7 ,35, 78, 92, 10]
largest = max(list3)
print("the largest number in the list is ", largest)

#smallest number in the list
list3  = [1, 2, 3, 7 ,35, 78, 92, 10]
smallest = min(list3)
print("the smallest number in the list is ", smallest)

#sum of the numbers in the list
list3  = [1, 2, 3, 7 ,35, 78, 92, 10]
addition = sum(list3)
print("addition of the numbers are" , addition)
 
#tuple-----imutable 
tuple1 = (1,2,3,4,5)
print(type(tuple1))

#for loop
for x in tuple1:
    print(x)


#Set----no duplicates and mutable

set1 = {1, 2, 3, 4, 5, 6, 7}
print(type(set1))

set1.add(8)
print(set1)

set1.pop()
print(set1)

#union
set2 = {1, 2, 5, 7, 8}
SetUnion= set1.union(set2)
print(SetUnion)

#intersection
set2 = {1, 2, 5, 7, 8}
SetIntersection= set1.intersection(set2)
print(SetIntersection)

#subset
SubSets = set1.issubset(set2)
print(SubSets)

#disjoint
SetDis = set1.isdisjoint(set2)
print(SetDis)

#dictionary ----key imutable --value mutable
dictionary1 = {1 : 20}
print(type(dictionary1))

studentdict = {
    "name" : "safura",
    "rollNo" : 2026,
    "RegNo" : 177
}
print(studentdict)

studentdict["name"] = "Safura"
print(studentdict)

print(type(studentdict))
print(len(studentdict))

StudentDict1 = studentdict.copy()
print(StudentDict1)                                                                                                                                                                                                                                                                                                             

if "age" in StudentDict1:
    print("yes it has name")
else:
    print("no it does not have")

