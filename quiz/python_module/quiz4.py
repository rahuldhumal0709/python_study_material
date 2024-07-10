# a, b, c=(1,2,3,4,5,6,7,8,9)[1::3]
# print(b)
# print(a)
# print(c)

# t1=('foo',)
# t2=('foo')
# t3=['foo']
# t4='foo'
# print("t1 : ",t1,type(t1))
# print("t2 : ",t2,type(t2))
# print("t3 : ",t3,type(t3))
# print("t4 : ",t4,type(t4))

# t=["foo","bar","baz"]
# t[1]="qux"
# #t[1:1]="qux"
# print(t)

# l=[1,2,3,4,5]
# l.remove(3)
# # del l[2]
# # l[2:3]=[]
# print(l)

# l1=[[1,2,3],[4,5,6]]
# l2=[]
# for list1 in l1:
#     l2.extend(list1)
# print(l2)

# a=["foo","bar","baz","qux","quux","corge"]
# print(a[4::-2])

# print(["a","b","c"]==["c","a","b"])
# a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[0::4]
# print("a",a,"\nb",b,"\nc",c)

a = [1, 2, 3, 4, 5]
a[2:3] = []
print(a)