# lst=[1,2,3,4]
# set1=set(lst)
# print(set1)
# print(lst[3])
# print(lst[-2])
# s="rahul"
# lst=s.split()
# print(lst)
# x=3.123
# print(int(x))

# print(64//2)
# print(65//2)
# print(66//2)

# print(1000<300)
# print(1000==300)

# print(66%5)

# print(5**3)

# print(3%4)
# a=2
# a=+1
# print(a)

# a=(1,2,3)
# b=(1,2,3)
# print(a is b)

# vowel="aeiou"
# lst=[]
# lst1=['a','e','o','u','e','a','a']
# for i in lst1:
#     if i not in vowel:
#         lst.append(i)
# print(lst)
# if lst:
#     print("hii")
# else:
#     print("hello")
# if {}:
#     print("wow we are here")
# else:
#     print("may be here")
#     if {0}:
#         print("but")
#     else:
#         print("and")

# str1="hello"
# c=0
# for x in str1:
#     print(x)
#     if(x!="l"):
#         c=c+1
# print(c)
# lst=[]
# t=()
# d={}
# print(type(lst),type(t),type(d))
# print(lst,t,d)
# a=5
# if a:
#     print(a)
# else:
#     print("False")
# for l in "jhon":
#     if l=="o":
#         pass
#     else:
#         print(l,end=",")

# for num in range(10,14):
#     for i in range(2,num):
#         if num%i==1:
#             print(num)
#             break

# for i in range(-2,-5,-1):
#     print(i,end=" ")
# x=0
# while x<100:
#     x=x+2
# print(x)
# var=10
# for i in range(10):
#     for j in range(2,10,1):
#         if var % 2 == 0:
#             continue
#             var=var+1
#     var=var+1
# else:
#     var=var+1
# print(var)

# lst=[10,20]
# lst1=['chair','table']
# for i in lst:
#     for j in lst1:
#         print(i,j)

# def f1():
#     global x
#     x=x+1
#     print(x)
# x=12
# print("x")
# f1()
# def f1(a,b=[]):
#     b.append(a)
#     return b
# print(f1(2,[3,4]))
# from re import S


# def f(p,q,r):
#     global s
#     # p=10
#     # q=20
#     # r=30
#     # s=40
#     print(p,q,r,s)
# p,q,r,s=1,2,3,4
# f(p,q,r)

# def f(x):
#     print("outer")
#     def f1(a):
#         print("inner")
#         print(a,x)
# f(3)
# f1(1)
# def printmax(a,b):
#     if a>b:
#         print("h")
#     elif(a==b):
#         print("e")
#     else:
#         print(b,'is maximum')
# printmax(3,4)
# def fun(a,b=5,c=10):
#     print("a is ",a,"and b is ",b,"and c is ",c)

# fun(3,7)
# fun(25,c=24)
# fun(c=50,a=100)
# def c(**check):
#     if check['isEven']%2==0:
#         print('even')
#     else:
#         print("odd")
# c(isEven=3)
# -----------------------------------------
# m=lambda x:x*2
# n=[1,2,3]
# d=map(m,n)
# lst=list(d)
# print(lst)

# l=["beach","car"]
# f=list(map(lambda w:f"{w} is fun",l))
# print(f)

# nums=[3,5,16,27]
# s=list(filter(lambda num : num<10, nums))
# print(s)

# def cube(n):
#     return n**3
# e=[2,4,6,8]
# res=map(cube,e)
# print(list(res))

# f=lambda x: return x
# print(f(2))
# n=[1,2,3]
# a=list(filter(lambda x:x%2==0,n))
# print(a)
# b=list(filter(lambda x:x>1,n))
# print(b)
# c=list(filter(lambda x:2,n))
# print(c)
# a={}
# a[2]=1
# print(a)
# a[1]=[2,3,4]
# print(a)
# print(a[1][1])
# print(a)