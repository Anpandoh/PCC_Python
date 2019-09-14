from Time_Class import Time
#Time Object 1
#myTime1 = Time()
#myTime1.print_time()
#myTime1.set_time(1,1,1)


#Time Object 2

myTime2 = Time()
myTime2.set_time(22,55,55)

#print("I know have 2 saved time values")
#myTime1.print_time()
myTime2.print_time()

myTime3 = Time()
myTime3.set_second(59)
myTime3.set_minute(59)
myTime3.set_hour(5)
myTime3.get_hour()
myTime3.get_second()
myTime3.get_minute()
myTime3.print_time()

#print (Time.__doc__)
#print (myTime1.__class__)
