'''
    In Python, strings are immutable. This means that once a string is created, its value cannot be changed directly. 
    When you use the replace() method on a string, it actually creates a new string with the specified replacements, 
    leaving the original string unchanged1
'''
str1 = 'DFPKH - 2024001 S'
str2 =''
for i in str1:
    if i == '4':
        i = '5'
        str2 = str2+i
    else:
        str2 = str2+i
print(str2)

str1 = str1.replace('2024','2025')
print(str1)

# str1 = [1,2,3,4,5]
# for i in range(len(str1)):
#     if str1[i]==4:
#         str1[i]=6
# print(str1)