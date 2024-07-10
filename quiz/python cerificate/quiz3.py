# my_str="abersi"
# k=[print(i) for i in my_str if i not in "aeiou"]
# class test:
#     def __init__(self,a="hello world"):
#         self.a=a

#     def display(self):
#         print(self.a)
def even_in():
    num=0
    while num<4:
        yield num
        num=num+2
o=even_in()
for i in range(2):
    next(o)
print(next(o))

# def f(x):
#     yield x+1
# g=f(8)
# next(g)
# print(next(g))

# cubes=(1,8,27,64,125,216)
# cube=iter(cubes)
# next(cube)
# print(next(cube))

# import itertools as it
# o=it.count(1,step=23)
# n=10
# while 0<n:
#     print(next(o))
#     n=n-1
# a=[1,2,3,4,5]
# b=['a','b','c']
# print(list(it.zip_longest(a,b)))
# o=it.chain(a,b)
# for i in range(3):
#     next(o)
# print(next(o))
class Animal:
    def __init__(self,name):
        print("Animal",end="")
        self.name=name
class Dog(Animal):
    def __init__(self,name,age):
        print("Dog",end="")
        super().__init__(name)
        self.age=age
yuki=Dog("yuki singh",4)
# print("abc"-"bc")
# print("abcd"[2:])
# class tester:
#     def __init__(self,id):
#         self.id=str(id)
#         id="224"
# temp=tester(12)
# print(temp.id)
# print(chr(ord("b")+1))

# d={"john":40,"peter":45}
# d.delete("john":40)
# print(d)

