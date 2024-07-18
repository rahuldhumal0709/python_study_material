'''
    lambda() : 
        - It is an anonymous funtion.
        - It can any no of parameters but only single expression(condition)
        - It doesnot have a return statement 
        - It helps to create one liner function

        Suntax - lambda arguments: expression
'''
def sum(num1,num2):
    return num1 + num2
result = sum(10,20)
print('Using normal function : ',result) 

lambda_sum = lambda num1,num2:num1+num2
result = lambda_sum(10,20)
print('Using lambda function : ',result)