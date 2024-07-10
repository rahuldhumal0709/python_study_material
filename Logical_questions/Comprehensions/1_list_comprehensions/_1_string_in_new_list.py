str=input("Enter a string : ")
#--------------------------------------------------------------1st way using Normal normal method
# lst=[]
# for i in str:
#     lst.append(i)
# print(lst)
#--------------------------------------------------------------2nd way using list comprehension
data=[i for i in str]
print(data)