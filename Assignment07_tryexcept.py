# ------------------------------------------------- #
# Title: Assignment 07
# Description: A simple demo of how error handing works in Python
# ChangeLog:
# qinlaura,11/29/2020,Created Script
# ------------------------------------------------- #

# ---------------Error Handling---------------------#

##### Basic try-except structure
print(1/0) # Python throws an error

try:
    print(1/0)
except:
    print('denominator is zero')

##### The exception classes
try:
    print(1/0)
except Exception as e:
    print(e)
    print(e.__class__)
    print(e.__doc__)
    print()
    # ZeroDivisionError

try:
    file = open('text.txt', 'r+')
except Exception as e:
    print(e)
    print(e.__class__)
    print(e.__doc__)
    print()
    # FileNotFoundError

try:
    dict = {'A':1, 'B':2}
    print(dict['C'])
except Exception as e:
    print(e)
    print(e.__class__)
    print(e.__doc__)
    print()
    # KeyError

##### catching specific exceptions
try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)
    print(e.__class__)
    print(e.__doc__)
    print()

try:
    file = open('text.txt', 'r+')
except ZeroDivisionError as e:
    print('Cant\'t divide by zero')
    print(e)
    print(e.__class__)
    print(e.__doc__)
    print()
    # note that the error isn't capture in except block
    # because only zero division errors are captured

try:
    file = open('text.txt', 'r+')
except ZeroDivisionError as e:
    print('Cant\'t divide by zero')
    print(e)
    print(e.__class__)
    print(e.__doc__)
except KeyError as e:
    print('Mapping key doesn\'t exist')
    print(e)
    print(e.__class__)
    print(e.__doc__)
except Exception as e:
    print('Other error')
    print(e)
    print(e.__class__)
    print(e.__doc__)
    # You can use multiple except blocks to make sure more
    # exception cases are captured

##### create your own custom exception class
class spaceInNameError(Exception):
    """File name must not include spaces"""
    def __str__(self):
        return('Do not use space in the file name')
    def __doc__(self):
        return('There should not be spaces in the file name for consistency')

try:
    filename = input('Enter a file name: ')
    if filename.find(' ') >= 0:
        raise spaceInNameError
    print(filename)
except Exception as e:
    print(e.__str__())
    print(e.__class__)
    print(e.__doc__())

raise spaceInNameError
