'''

1. append()
The append() method is used to add elements at the end of the list. This method can only add a single element at a time.

'''

list1 =['A','B','C','D']
list1.append('E')
print(list1)


'''

2. extend()
The extend() method is used to add more than one element at the end of the list. Although it can add more than one element, unlike append(), it adds them at the end of the list like append().

'''

list1.extend(['F','G'])
print(list1)

'''

3. insert()
The insert() method can add an element at a given position in the list. Thus, unlike append(), it can add elements at any position, but like append(), it can add only one element at a time. This method takes two arguments. The first argument specifies the position, and the second argument specifies the element to be inserted.

'''

list1.insert(3,'Insert')
print(list1)   


'''

4. remove()
The remove() method is used to remove an element from the list. In the case of multiple occurrences of the same element, only the first occurrence is removed.

'''

list1.remove('F')
print(list1) 

'''

5. pop()
The method pop() can remove an element from any position in the list. The parameter supplied to this method is the index of the element to be removed.

'''

list1.pop(3)
print(list1) 


'''

6. slice
The slice operation is used to print a section of the list. The slice operation returns a specific range of elements. It does not modify the original list.

'''

print(list1[:4])  # prints from beginning to end index
print(list1[2:])  # prints from start index to end of list
print(list1[2:4]) # prints from start index to end index
print(list1[:])   # prints from beginning to end of list

'''

7. reverse()
The reverse() operation is used to reverse the elements of the list. This method modifies the original list. To reverse a list without modifying the original one, we use the slice operation with negative indices.

'''

print(list1.reverse())

'''

8. len()
The len() method returns the length of the list, i.e. the number of elements in the list.

'''
print(len(list1))

'''

9. min() & max()
The min() method returns the minimum value in the list. The max() method returns the maximum value in the list. Both the methods accept only homogeneous lists, i.e. list having elements of similar type.

'''

print(min([1, 2, 3]))
print(max([1, 2, 3]))

'''

10. count()
The function count() returns the number of occurrences of a given element in the list.

'''
print(list1.count(3))


'''

11. concatenate
The concatenate operation is used to merge two lists and return a single list. The + sign is used to perform the concatenation. Note that the individual lists are not modified, and a new combined list is returned.

'''

list2 ='Hi, '
list3 = 'Hello'

print(list2 + list3)

'''

12. multiply
Python also allows multiplying the list n times. The resultant list is the original list iterated n times.

'''

print(list2*3)

'''

13. index()
The index() method returns the position of the first occurrence of the given element. It takes two optional parameters – the begin index and the end index. 

'''

print(list1.index('B'))


'''

14. sort()
The sort method sorts the list in ascending order. This operation can only be performed on homogeneous lists, i.e. lists having elements of similar type.

'''

yourList = [4, 2, 6, 5, 0, 1]
yourList.sort()
print(yourList)

'''

15. clear()
This function erases all the elements from the list and empties them.

'''

yourList.clear()
print(yourList)