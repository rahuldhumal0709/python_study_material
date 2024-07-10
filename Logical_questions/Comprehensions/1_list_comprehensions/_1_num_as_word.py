# 423 - take input from user
# o/p : Four Two Three
#---------------------------------------------------Normal way
# num=int(input())
# str1=str(num)
# lst=[]
# d={'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
# for i in str1:
#     lst.append(d[i])
# for j in lst:
#     print(j,end=" ")
# print()
# ----------------------------------------------------------------------------list comprehension
num=int(input("Enter a number : "))
str1=str(num)
d={'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
data=[d[i] for i in str1]
for j in data:
    print(j,end=" ")
print()