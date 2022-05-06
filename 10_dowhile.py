'''

do
{
    Statement(s)
} while (condition);

--> In Python, there is no dedicated do while conditional loop statement, and so this function is achieved by creating a logical code from the while loop, if statement, break and continue conditional statements. When the logic of the program is done correctly, depending on the requirement provided, the Do While loop can be imitated perfectly.


'''

i = 1
while True:  # Any true condition like 1 == 1
    print(i)
    i = i + 1
    if(i > 5):
        break