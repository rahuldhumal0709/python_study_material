# odd=lambda x:bool(x%2)
# n=[n for n in range(10)]
# print(n)
# n=list()
# for i in n:
#     if odd(i):
#         continue
#     else:
#         break
# fun=lambda y:bool(y%2)
# print(fun(25), fun(31))
# import functools
# l=[1,2,4,5]
# print(functools.reduce(lambda x,y:x*y,l))
# l=[1,-2,-7,4,10]
# def f1(x):
#     return x<2
# m1=filter(f1,l)
# print(list(m1))
# l=[-2,4]
# m=map(lambda x:x*2,l)
# print("address of m",list(m))
# l=[1,-2,-4,4,6]
# def f1(x):
#     return x<-1
# m1=map(f1,l)
# print(list(m1))
# l=list(map((lambda x:x^3),range(5)))
# print(l)
# w=['bay','cat','boy','fan']
# b=list(filter(lambda w: w.startswith('b'),w))
# print(b)
a=[x**2 for x in range(10)]
b=list(map((lambda y: y**2),range(10)))
print(a==b)