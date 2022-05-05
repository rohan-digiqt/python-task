'''

- Variables are containers for storing data values.
- A variable is created the moment you first assign a value to it.
- Variables do not need to be declared with any particular type, and can even change type after they have been set.

'''
x = 5
y = 'Rohan'
print(x,y)

a = 4           # a is of type int
print(a)
a = "Hello"     # a is of type string
print(a)

'''

Typecasting:
-> If you want to specify the data type of a variable, this can be done with casting.

'''

b = str(3)      # x is '3'
c = int(3)      # x is 3
d = float(3)    # x is 3.0

# Get the type of variable

print(type(b))
print(type(c))
print(type(d))

# In a string single quotes and double quotes are same.
# Variable's name is case sensitive. a and A is diffrent.

# Many Values to Multiple Variables

aA, bB, cC = "One", "Two", "Three"
print(aA)
print(bB)
print(cC)

# Note: Make sure the number of variables matches the number of values, or else you will get an error.

''' One Value to Multiple Variables '''

dD = eE = fF = "Same Value"
print(dD)
print(eE)
print(fF)

''' 

Unpack a Collection:
-> If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

'''

colors = ['Red', 'Orange', 'Blue']
gG, hH, iI = colors
print(gG)
print(hH)
print(iI)

'''

Global Variable
-> Variables that are created outside of a function (as in all of the examples above) are known as global variables.
-> Global variables can be used by everyone, both inside of functions and outside.

'''

kK = "awesome"

def myfunc():
  kK = "fantastic"
  print("Python is " + kK)

myfunc()

print("Python is " + kK)

'''

The global Keyword
-> Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
-> To create a global variable inside a function, you can use the global keyword.

'''

def myfunc():
  global mM
  mM = "fantastic"

myfunc()

print("Python is really " + mM)