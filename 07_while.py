i = 1
while i <= 5:
    print(i)
    i += 1 # i = i + 1

'''

Break Statement:
-> With the break statement we can stop the loop even if the while condition is true.

'''
while i < 6:
    print(i)
    if i == 3:
        break
    i = i + 1

'''

Continue Statement:
-> With the continue statement we can stop the current location, and continue with the next.

'''
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)

j = 6

while j < 5:
    j += 1
else:
    print(j)