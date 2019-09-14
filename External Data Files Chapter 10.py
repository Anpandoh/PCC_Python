
import pickle
letters = ['a', 'b', 'c'] 
pickled_letters = pickle.dumps(letters)

print(pickled_letters)

import shelve
db_file = shelve.open('A:/High School/Python Summer/letters.txt', 'c')
db_file ['vowels'] = ['a', 'e', 'i', 'o', 'u'] 
db_file ['end'] = ['x', 'y', 'z'] 
db_file.close()
