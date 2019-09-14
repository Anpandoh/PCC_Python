try:
    counter = 1
    while (counter >= 1):
       number = 2.0 ** counter
       counter = counter + 0.001
       print(number)

except OverflowError as oe:
    print(oe)
    print('Your number is:',number)

except KeyboardInterrupt as k:
    print ('Your number is:',number)
    print (k)
