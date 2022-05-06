'''

For Loop:

-> A for loop is used for iterating over a sequence that is either a list, a tuple, a dictionary, a set, or a string.

'''

numbers = ['One', 'Two', 'Three']
for x in numbers:
    print(x)

# For loop in string

for y in 'Rohan':
    print(y)

# Range in for loop

for z in range(5):
    print(z)
else:
    print('Loop run successfully')

# Nested for loop

numS = ['One','Two','Three']
numD = [1, 2, 3]

for x in numS:
    for y in numD:
        print(x,y)