myList = ['Cricket','Hockey','Football']
print(myList[1])

'''

Negative Indexing:

-> -1 refers to the last item
-> -2 refers to the last item

'''

print(myList[-1])

'''

Range of Indexing:

-> You can specify a range of indexes by specifying where to start and where to end the range.

-> When specifying a range, the return value will be a new list with the specified items.

'''

myList2 = ['A','B','C','D','E','F','G','H','I']
print(myList2[2:5]) # start(included) end(not-included)

# Check item exits or not

if 'R' in myList2:
    print('Exits')
else:
    print('Not Exits')