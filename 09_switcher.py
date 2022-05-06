def getInput ():
    f_num = int(input('Enter First Number: '))
    s_num = int(input('Enter Second Number: '))
    return f_num,s_num

def add():
    x,y = getInput()
    print(x + y)

def sub():
    x,y = getInput()
    print(x - y)

def mul():
    x,y = getInput()
    print(x * y)

def div():
    x,y = getInput()
    print(x / y)

print('''
1. Addition
2. Substraction
3. Multiplication
4. Division
''')

choice = int(input('Enter your choice: '))

def operations(choice):
    switcher = {
    1: add(),
    2: sub(),
    3: mul(),
    4: div(),
    }
    return switcher.get(choice, 'Invalid Input')

ans = operations(choice)
print(ans)