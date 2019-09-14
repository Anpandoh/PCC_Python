my_list = []
value = 0
a = eval(input("Enter value to be included in average(-999 quits):\n"))
while (a != -999):
    my_list = my_list + [a]
    a = eval(input("Enter a value to be included in average(-999 quits):\n"))

b = len(my_list)
if b != 0:
    for x in range(b):
        value = value + my_list[x]
    print("Your average is:", value/b)
    
    F = input("Do you want to see the numbers you averaged?\n")
    if F == "yes" or F == "Yes" or F == "y":
        print(my_list)
        
else:
    print("No values were entered(-999 quits)")
