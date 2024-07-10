# Lambda Function
# it is a anonymous(unnamed) function
# it is a function without a name
# it can any no of parameters but only single expression(condition)
# it doesnot have a return statement 
# it helps to create one liner function

# def add(a,b):
#     return a+b
# result = add(6,7)
# print(result)

# syntax : lambda <argument1,argument2> : <expression>
# res = lambda a,b : a+b
# print(res(6,7))

def add(n):
 return lambda a : a + n
res = add(6)
print(res(7))