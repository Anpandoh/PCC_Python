number = 1
while number <= 100:
    print(number)
    number = number + 9

for number in range(1,6):
        print (number)
print ("goodbye!")

Amount_of_Numbers = eval(input("How many numbers do you want to average?\n"))
totl = 0.0
for a in range(Amount_of_Numbers):
    b = eval(input("Give me a Value\n"))
    totl = totl + b

Average = totl/Amount_of_Numbers                         
print("Your average is",Average)                         
phrase = ("Hello, my name is Aneesh Pandoh")
print(phrase)
answer = input("Yes or No \n")
phrase = (phrase[7:])
phrase = 'M'+(phrase[1:])
while answer == 'yes' or answer == 'Yes' or answer == 'y':
    print(phrase)
    phrase = phrase + '!'

