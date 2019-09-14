Amount_of_Numbers = eval(input("How many numbers do you want to average?(-1 is not permitted)\n"))
total = 0.0
for a in range(Amount_of_Numbers):
    b = eval(input("Give me a Value\n"))
    if b != -1:
        total = total + b
    else:
        print("This value is not permitted")
        break
        
    
Average = total/Amount_of_Numbers
if b != -1:
    print("Your average is",Average)  
