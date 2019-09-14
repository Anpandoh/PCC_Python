print ("This program will give you an example of how slicing works")
phrase = input("Give me a phrase to use:\n")

a = eval(input("Enter the number of letters you want the start of your sliced phrase to be:\n"))-1
b = eval(input("Enter the number of letters you want the end of your sliced phrase to be:\n"))-1

print (phrase[a:b])
               
