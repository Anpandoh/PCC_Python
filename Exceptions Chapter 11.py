infile = open('data.txt', 'w')
infile.write('Aneesh')
infile.flush()
infile.close()
try:
   infile = open('data.txt', 'r')
   try:
       value = infile.readline()
       number = int(value)
       print (number)
   finally:
       infile.close()
       print ("the data file was closed")
except IOError as io:
   print ("Could not open file:", io.filename)
except ValueError:
   print ("Could not convert", value, "to a number")
