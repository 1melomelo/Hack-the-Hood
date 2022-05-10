"""" Commonly Used Data Structures
     in Python
"""
# 3 data types we will work most closely with
# 1. Strings
# 2. Lists
# 3. Dictionaries

# Sequence Types
# Sequence = an ordered set of some data type or types,
#            in which you can access different pieces of data 
#            using the sequence's INDEX
#            = INDEX starts @ 0; but can be done with + or - numbers
# Ex: Strings, Lists

### STRINGS 
# = a list of text characters
# can access using an index

# 3 ways to add elements to a string
# 1. Add elements using + or += operator
# 2. Add elements using str.join() method
# 3. Add strings together using Python f-strings

# 3 methods for adding elements to a list using list class methods:
# 1. list.append()  = adds an element to end of list
odd = [1,3,5]
odd.append(7)
# Output: [1,3,5,7]

# 2. list.extend()  = adds a list to the end of another list
odd = [1,3]
odd.extend([5,7])
# Output: [1,3,5,7]

# 3. list.insert()  = adds an element to a list @ a specific index
odd = [1,5]
odd.insert(1,3)
# Output: [1,3,5] 
# inserted 3 at index 1 (2nd from left of list)

## String Examples: Using Operators
from unicodedata import name

fname = "Lady"
mname = "Gaga"

# printing fname string
print("The first name: " + str(fname))
# output: The first name: Lady

# printing mname add string
print("The middle name : " + str(mname))
# output: The middle name: Gaga

# Using += operator adding one string to another
fname += name

# print result
print("The concatenated string is: " + fname)
# output: Thje concatenated string is: LadyGaga

## String Examples: str.join()

# Create a list of strings
listofStrings = [fname,mname]
finalString ="".join(listofStrings)

# print the final result
print("The appended string is: " + finalString)
# output: The appended string is: LadyGaga

## 2 Techniques to REMOVE ELEMENTS from a string
# 1. Use str.replace()
str = "Engineering"
print("OIriginal string: " + str)
# Output = Original string: Engineering

res_str = str.replace('e','')
# removes all occurrences of 'e'
print("The string after removal of character: " + res_str)
# Output = The string after removal of character: Enginring

# removes 1st occurrence of e
res_str = str.replace('e', '', 1)
print("The string after removal of character: " + res_str)
# Output = The string after removal of character: Enginering


# 2. Use slicing
# SLICING = the process of obtaining a portion or subset of a sequence via indices
# can be done with both strings & lists

# Template for slicing a subset of a sequence & obtaining a substring
# sequence[start:end]

# start = the index from where we want the subset to start
# end = the index where we want our subset to end
# The character @ the end index in the string will not be included in substring
# obtained through this method.

# An Example:
my_string = "This is MY string!"
print(my_string[0:4]) # From the start till before the 4th index
# Output = This
print(my_string[1:7])
# Output = his is
print(my_string[8:len(my_string)]) # From the 8th index till the end
# Output = MY string!

# 3 methods for REMOVING ELEMENTS from a list
# 1. list.remove() = removes a specific element from a list
even = [1,3,5]
even.remove(5)
# Output = [1,3]

# 2. list.pop() = removes & returns an element @ a specific index
even = [1,3,5]
even.pop(1)
# Output = [1,5]

# 3. list.clear() = removes all elements currently in a list
even = [1,3,5]
even.clear()
# Output = []

## LISTS
#  stores all relevant pcs of info in 1 place
songs = ["ROCKSTAR" , "Do It", "For The Night"]

### DICTIONARIES
#    Central Data Structure
#    Unordered; have an index
#    Can store any # of values which can even be other data structures 
#    & each is identified by a unique key
#    Allow to store data with more emphasis on its relationships
#    Store data in key:value pairs
#    Each key must be unique
#    How to add items to a dictionary: create a new key with the same
#    square bracket notation to access already existing keys
#    How to delete pairs: accessing them with square bracket  notation
#    & pairing it with del keyword

capital = {"Argentina": "Buenos Aires",
          "Bolivia": "La Paz",
          "Brazil": "Brasilia"}

# Access dictionary elements via the key.
capital["Brazil"] = "Brasilia"






