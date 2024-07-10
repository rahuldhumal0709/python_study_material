lst = [4,5,61,2,8,10,11]
# #--------------------------------------------------------------1st way using Normal function 
# def even(lst):
#     even_lst = []
#     for i in lst:
#         if i%2==0:
#             even_lst.append(i)
#     return even_lst
# elst = even(lst)
# print(elst)
# #--------------------------------------------------------------2nd way using filter function
# def even(lst):
#     return lst%2==0
# fil_lst = list(filter(even,lst))
# print(fil_lst)
# #--------------------------------------------------------------3nd way using lambda with filter function
# # syntax : lambda <arguments> : <expressios>
lambda_lst = list(filter(lambda lst : lst%2==0,lst))
print(lambda_lst)