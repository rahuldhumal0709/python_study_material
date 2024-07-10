# def s(name,no=20):
#     print(name,no)
# s('Ena',25)

# s='apple mango kiwi'
# def t(f1,f2,f3):
#     print('I love to eat',f2)
# t(*tuple(s.split(' ')))

# def outerFun(a,b):
#     def innerFun(c,d):
#         return c+d
#     return innerFun(a,b)
#     return a
# result=outerFun(5,10)
# print(result)

# def fun1(num):
#     return num+25
# fun1(5)
# print(num)

# def fun1(*data):
#     print(data)
# fun1(10,20)

# def dp(**args):
#     for i in args:
#         print(i)
# dp(name='emma',age=25)

# gp={'tshirts':'Duke NumeroUno Versache','shorts':'nike,ABIBAS,PAMA'}
# def ingoa(tshirts,shorts):
#     print('I should wear',tshirts.split(' ')[0])
# ingoa(**gp)
# import random

# print(random.randint(10,210))

# x=[1,2,4,6]
# if x.sort():
#     print(x)

# x = 75
# def myfun():
#     x=x+1
#     print(x)
# myfun()
# print(x)

# x = 'happy'
# def sum(a):
#     global x
#     x='sad'
# sum('mango')
# print(x)

# x = 'happy'
# def sum():
#     print(x)
#     x='sad'
# sum()
def tf(a,b):
    print('a is ',a)
    print('b is ',b)
tf(5,25)