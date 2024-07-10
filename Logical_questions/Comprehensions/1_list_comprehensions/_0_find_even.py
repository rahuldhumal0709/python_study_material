lst = [4,5,61,2,8,10,11]
#--------------------------------------------------------------1st way using Normal normal method
# lst1 = []
# for i in lst:
#     if i%2==0:
#         lst1.append(i)
# print(lst1)
# #--------------------------------------------------------------2nd way using list comprehension
data=[i for i in lst if i%2==0]
print(data)