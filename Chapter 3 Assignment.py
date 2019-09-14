category = eval(input("What is the wind speed (mph) of the hurricane?\n"))
if category >=74 and category <= 95:
    print("This is a Category 1 hurricane")
elif category >=96 and category <= 110:
    print ("This is a Category 2 hurricane")
elif category >=111 and category <=130:
    print ("This is a Category 3 hurricane")
elif category >= 131 and category <=155:
    print("This is a Category 4 hurricane")
elif category > 155:
    print("This is a Category 5 hurricane")
else:
    print("Not a hurricane")
