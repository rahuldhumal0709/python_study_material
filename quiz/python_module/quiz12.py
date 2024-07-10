# def convI(s):
#     try:
#         num= int(s)
#         print("success")
#     except TypeError:
#         print('Failed')
#         num=-1
# l=[1,2,3]
# convI(l)
# try:
#     f=open("demofile.txt")
#     f.write("welcome")
# except:
#     print("something went wrong")
# finally:
#     f.close()
# x=10
# y=8
# assert x>y, 'x too small'
# class array:
#     def __init__(self,fix_size):
#         self.fix_size = fix_size
#         self.length   = 0
#         self.data     = []
    
#     def add(self,element):
#         if self.length < self.fix_size:
#             self.data.append(element)
#             self.length += 1
#         else:
#             print("Array is full")
#     def insert(self,index,ele):
#         if self.length < self.fix_size:
#             self.data.insert(index,ele)
#             self.length += 1
#         else:
#             print("Array is full")
#     def remove(self,ele1):
#         self.data.remove(ele1)
#         self.length -= 1
#     def pop(self,index1):
#         self.data.pop(index1)
#         self.length -= 1
# obj = array(5)
# obj.add(10)
# obj.add(20)
# obj.add(30)
# obj.add(40)
# print(obj.data)
# obj.insert(2,50)
# print(obj.data)
# obj.remove(10)
# print(obj.data)
# obj.pop(1)
# print(obj.data)
# from operator import not_


# def fun(singleLL=[10,20,30,40]):
#     prev=None
#     current = singleLL.head
#     while current is not None:
#         next=current.next
#         current.next=prev
#         prev=current
#         current=next
#     singleLL.head=prev
#     return singleLL
# a=fun()
# print(a)
# a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# print(a[5::-2])