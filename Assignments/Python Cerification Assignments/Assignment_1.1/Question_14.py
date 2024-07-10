# Q14. Write a program to count occurrences of all characters within a string.

# str1 = input("Enter a string : ")
# # char_dict = dict()
# # for char in str1:
# #     count = str1.count(char)
# #     char_dict[char] = count
# # print('Result:', char_dict)
# str1=['abc']
# dict1={i:str1.count(i) for i in str1}
# print(dict1)
str1=["abc","abcd","ab"]
dict1={i:len(i) for i in str1}
print(dict1)