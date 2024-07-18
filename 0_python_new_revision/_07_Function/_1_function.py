'''
Function : 
    - A function is a block of code that performs a specific task.
    - Functions making code more readable, and easier to maintain.
    - Functions can take inputs, perform operations, and return outputs.
    - To define a function in Python, you use the 'def' keyword.
'''

def addition():               # defining the function
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    add = no1 + no2
    print("Addition : ",add)
addition()                    # calling the function