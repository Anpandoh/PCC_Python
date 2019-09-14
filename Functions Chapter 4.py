def printwelcome():
    """This code welcomes the user to the program"""
    print ("Welcome to my program")
    print ("I hope you like it")

printwelcome()
print (printwelcome())
def changevalue(value):
    """This functon changes the value passed into 1"""
    print ("Inside, value is:", value)
    value = 1
    print("Inside, value is changed to:", value)

number = 5
print("Outside the number is:", number)
changevalue(number)
print ("Outside, number is now:", number)

#after global statement
print()
def changevalue():
    """This function changes the value passed in to 1(global)"""
    global number
    number = 1

changevalue()
print ("Outside, number is now:",number)
print("\n"*3)
def square(num):
    """This finds the ^2 of a number"""
    result = num * num
    return result

for i in range(1,11):
    print(square(i))
print("\n"*3)

#this version gives the function a default value of 1 if no number is specified
def square(num = 1):
    """This function calculates the square of a number"""
    result = num*num
    return result
print (square( ))

#You are also allowed to give specific values to certain variables in the function
