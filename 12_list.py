'''

Types of Lists:

1. A Simple List
2. Negative Indexing in List
3. Accessing Element/Item
4. Beginning Range
5. Ending Range
6. Interchanging Element
7. Loop in List
8. Length of List
9. Adding Element in List

'''
'''

List:

-> Lists are used to store multiple items in a single variable.

-> Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

-> Lists are created using square brackets:

'''

# Creation of List

nameList = ['Rohan','Tanmay','Amit','Neel','Rushi']
print(nameList)

'''

List Items:

-> List items are ordered, changeable, and allow duplicate values.

-> List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered:

-> When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

-> If you add new items to a list, the new items will be placed at the end of the list.

Changeable:

-> The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates:

-> Since lists are indexed, lists can have items with the same value:
'''

'''

List Length:

-> To determine how many items a list has, use the len() function:

'''
print(len(nameList))

myList = ['Rohan',50.55, True]
print(myList)

# Type

print(type(myList))
print(type(nameList))


# List Constructor

'''

Constructor: 

-> Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created.

'''

myList2 = list(('Mango','Apple','Banana')) # Note the double round brackets
print(myList2)

# Adding Element

myList2.append('Orange')
print(myList2)