import shelve
testscores = shelve.open('student_scorecard.txt','c')

number_of_students = eval(input("How many students have taken the test?\n"))

for x in range(number_of_students):
    if x != (number_of_students):
        print("------------------------------------------------------------")
        print("Student" , x+1)
    name = input("What is the student's name?\n")
    score = eval(input("What is his/her score?\n"))
    testscores [name] = score
    
print("------------------------------------------------------------")
print("------------------------------------------------------------")

question = input("Do you want to find a student's test score?\n")

if question == "yes" or question == "Yes" or question == "y":
    while question == "yes" or question == "Yes" or question == "y":
        search_name = input("What is the name of the student?\n")
        print("Their score is:",testscores.get(search_name, "not found"))
        print("------------------------------------------------------------")
        question = input("Do you want to search for another name?\n")
        
    print("Thank you for your time")

else:
    print("Thank you for your time")

testscores.close()
testscores.sync()
