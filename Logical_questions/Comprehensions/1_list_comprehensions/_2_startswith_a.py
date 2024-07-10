lst = ["apple","mango","Aeroplane","ac","laptop","diary","mobile"]
#--------------------------------------------------------------1st way using Normal normal method
# lst1=[]
# for i in lst:
#     if (i.startswith('a') or i.startswith('A')) and len(i)>4:
#         lst1.append(i)
# print(lst1)
# #--------------------------------------------------------------2nd way using list comprehension
data=[i for i in lst if (i.startswith('a') or i.startswith('A')) and len(i)>4]
print(data)