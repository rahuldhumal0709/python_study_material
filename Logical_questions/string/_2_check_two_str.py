str1 = "Python is a programming language" # take input from user
str2 = "HTML is a markup language"        # take input from user
# o/p : Python programming HTML markup
#---------------------------------------------------Normal way
# str1 = input("Enter 1st string : ")
# str2 = input("Enter 2nd string : ")
lst1=str1.split(" ")
lst2=str2.split(" ")
lst=[]
for i in lst1:
    if i not in lst2:
        lst.append(i)
for j in lst2:
    if j not in lst1:
        lst.append(j)
for k in lst:
    print(k,end=" ")
print()
#---------------------------------------------------------------------------list comprehension
# str1 = input("Enter 1st string : ")
# str2 = input("Enter 2nd string : ")
lst1=str1.split(" ")
lst2=str2.split(" ")
data=[[i for i in lst1 if i not in lst2],[j for j in lst2 if j not in lst1]]
for s in data:
    # print(s,end=" ")
    for s1 in s:
        print(s1,end=" ")
print()