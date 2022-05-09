# Initializing list using square brackets

nameList = ['Rohan','Tanmay','Amit','Neel','Rushi']
print(nameList)

# Initializing using list() method

myList2 = list(('Mango','Apple','Banana')) # Note the double round brackets
print(myList2)

# Initialization of list using list comprehension method
# -> In this method we see range method in the for loop to create and initialize list. This method can be used to create any iterable other list using the existing iterable object such as range().

courses = [n for n in range(6)]
print(courses)

# Initialization of list using list multiplication
# -> In this method we use * operator or list multiplication method for initializing the list. This method is one of the fastest method. This method is also similar to list comprehension method with repeat() method. This method is also used when we want to initialize and create a list with specific number of redefined values of the items in the list.

char = ['Rohan']*5
print(char)