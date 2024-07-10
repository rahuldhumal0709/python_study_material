# class dog:
#     def walk(self):
#         return "walking"

#     def speak(self):
#         return "Woof"

# class Jack(dog):
#     def talk(self):
#         return super().speak()

# b=Jack()
# print(b.talk())
import re
# s="we are humans"
# m=re.match(r'(.*)(.*?)(,*)',s)
# print(m.groups())
# t=[1,2,3,4,5]
# td=t
# print(id(t)==id(td))
# x='abcd'
# for i in range(len(x)):
#     print(i.upper())
# n=[1,2,3]
# a=list(filter(lambda x:(x+1)*3/3%3==0,n ))
# print(a)
# s1={1,2,3}
# s2={3,4,5}
# a=s1.union({3,4,5})
# b=s1.union([3,4,5])
# c=s1.union(set([3,4,5]))
# print(a)
# # print(b)
# # print(c)

# x=['ab','cd']
# print(list(map(len,x)))

# d={"foo":100,"bar":200,"baz":300}
# print(d)
# d={"id":101,"name":"ABC"}
# a=d.setdefault("name","PQR")
# print(a)
# x=["A","b",{"foo":1,"bar":{"x":10,"y":20,"z":30},"baz":3},"c","d"]
# print("z" in x[2])
# i=1
# while i<20:
#     if i%2==0:
#         break
#     print(i)
#     i+=2
# def myfun(x,y,z,a):
#     print(x+y)
# nums=[1,2,3,4]
# myfun(*nums)
# s="foo"
# t="bar"
# print("barf" in 2*(s+t))
# d={"One":1,2:"Two",3:"Three",4:"Four"}
# print(3 in d)
# s="python,java,c,c++"
# print(s[10:1:-2])
# r=re.compile("\d+[a-z]")
# s="abc1234def4567abcd89"
# l=re.findall(r,s)
# print(l)
# d={"a":0,"b":1,"c":0}

# if d["a"]>0:
#     print("ok")
# elif d["b"]>0:
#     print("ok")
# elif d["c"]>0:
#     print("ok")
# elif d["d"]>0:
#     print("ok")
# else:
#     print("not ok")

# def outerFun(a,b):
#     def innerFun(c,d):
#         return c+d
#     return innerFun(a,b)
# res=outerFun(5,10)
# print(res)

# sum=0
# for i in range(4):
#     sum+=i
# print(sum)
# sum(34,23)
# class A:
#     def test1(self):
#         print("test of A Caled")
# class B(A):
#     def test(self):
#         print("test of B Caled")

# class C(A):
#     def test(self):
#         print("test of C Caled")

# class D(B,C):
#     def test2(self):
#         print("test of D Caled")
# o=D()
# o.test()
d1={"john":40,"peter":45}
d2={"john":40,"peter":45}
print(d1==d2)

# given="apple mango kiwi"
# def test_fun(fruit1,fruit2,fruit3):
#     print("I love to eat",fruit2)
# test_fun(*tuple(given.split(' ')))

# class A:
#     def __init__(self):
#         self.__x=1
# class B(A):
#     def dis(self):
#         print(self.__x)
# def main():
#     o=B()
#     o.dis()
# main()
        
# def d(f):
#     def n(*args):
#         return '$'+str(f(*args))
#     return n
# @d
# def p(a,t):
#         return a+a*t
# print(p(100,0))
