'''
This is a note for Module 3 of Python Intermediate. 
This is a Multi-line String comment. 

LESSON 1: Python Dictionaries

# There are four collection data types in the Python programming language: List, Tuple, Set, and Dictionary.

https://www.w3schools.com/python/python_dictionaries.asp

'''
# Dictionaries are used to store data values in --> key: value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
# The values in dictionary items can be of any data type:

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)
print()

# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Accessing Items
print(thisdict["brand"])
print()
x = thisdict.get("model")
print(x)
print("----")

# Get Keys
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)
x = thisdict.items()
print(x)
x = thisdict.update({"brand": "Toyota"})
x = thisdict.items()
print(x)
print()



# To get the length
print(len(thisdict))


# It is also possible to use the dict() constructor to make a dictionary.
newdict = dict(name = "John", age = 36, country = "Norway")
print(newdict)



