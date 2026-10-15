# The Student Grading System
# Create a dictionary where the keys are the names of 5 students and the values 
# are their marks out of 100 (e.g.,
# {"Ali": 85, "Ayesha": 92} ). Use a for loop to iterate through the dictionary.
# Use if/elif/else statements to assign and print a grade for each student based on their marks
#  (A: 90+, B: 80-89, C: 70-79, F: <70).

studentdict = {
    "ali" : 76,
    "sara" : 65,
    "sana" : 89,
    "ahmad" : 79,
    "anaya" : 93,
}
for name, marks in studentdict.items():
    if marks >= 90 and marks <= 100:
        print("grade A+")
    elif marks >= 80 and marks <= 89:
        print("grade B")
    elif marks >= 70 and marks <= 79:
        print("grade C")
    elif marks < 70 :
        print("graade F")  


    
    
    
    
    
        

       





 