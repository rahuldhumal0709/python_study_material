'''
    Exception Handling :
        - Exception handling allows you to manage errors gracefully during the execution of a program.
        - 'try' Block: Contains code that might raise an exception.
        - 'except' Block: Catches and handles the exception.
'''
import traceback
while(True):
    try:
        num1 = int(input('Enter num1 : '))
        num2 = int(input('Enter num2 : '))
        print('Addition is : ',num1+num2)
    except Exception as ex:
        traceback.print_exc()