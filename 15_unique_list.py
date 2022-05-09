'''

Unique List:

-> Python's unique list is a list that contains unique elements irrespective of the order

'''

'''

Method #1 - Using the Traversal

-> n this method, the items on the list are traversed individually. Then the items are added or can append the item in the unique list if the item is not in a unique list. This can be done by simple for loop and if statements. Below is the code for this method.

'''

def unique_py (uList):
    unique_list = []

    for n in uList:
        if n not in unique_list:
            unique_list.append(n)
    print(unique_list)

list1 = [10,20,30,40,10,20,30]
unique_py(list1)


'''

Method #2 - Using set () property

-> set(), which has iterable arguments which are distinct elements. Using this property checks for the unique items and appends these unique items of the list to set. The main difference between list and set is that the list allows us to insert duplicate elements, but the set does not have duplicate elements as the elements are inserted only once, even if it's inserted more than once. 

'''

def py_unique(lis1):
    set_list = set(lis1)
    u_list = list(set_list)
    print(u_list)

list1 = [10,20,30,40,10,20,30]
py_unique(list1)


'''

Method #3 – Using Python Library numpy

'''

import numpy as nump

l1 = nump.unique(list1)
print(l1)