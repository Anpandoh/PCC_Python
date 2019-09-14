a = input("Do you want to print a table of temperatures and their fahrenheit equivalents between 0 and 100?\n")
def tempconv(Cdegrees):
    Fahrenheit = Cdegrees * 1.8 + 32
    return Fahrenheit
if a == "yes" or a == "y" or a == "Yes":
    for x in range(0,101,10):
         print("Celsius",x,"\tFahrenheit", tempconv(x))
    
else:
    print("Ok")

    
    
