# Enter a string : KLRAHUL
# {'K': 1, 'L': 2, 'R': 1, 'A': 1, 'H': 1, 'U': 1}
#---------------------------------------------------Normal way
# str = input("Enter a string : ")
# dict2= {}
# for i in str:
#     dict2[i]=str.count(i)
# print(dict2)
#-------------------------------------------------dict comprehension
str = input("Enter a string : ")
dict1 = {i:str.count(i) for i in str} 
print(dict1)