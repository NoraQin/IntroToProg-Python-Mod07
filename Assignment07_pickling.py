# ------------------------------------------------- #
# Title: Assignment 07
# Description: A simple demo of how pickling works in Python
# ChangeLog:
# qinlaura,11/29/2020,Created Script
# ------------------------------------------------- #

# ---------------Pickling---------------------#

##### import the pickle package for processing binary data
import pickle

##### create a binary file for writing
outlist = open('grocery_list.txt', 'wb')

##### write new data into the binary file
grocery = [['onions','carrots','milk','egg'], ['cheese', 'crackers'], 'chicken']
pickle.dump(grocery, outlist)
outlist.close()

##### read a binary file
inlist = open('grocery_list.txt', 'rb')
print(pickle.load(inlist))
print(pickle.load(inlist)) # EOF


