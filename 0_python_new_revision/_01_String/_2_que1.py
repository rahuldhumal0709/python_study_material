# Write a program to print ASCII value of A-z and store in a list.
lst = []
for char in range(ord('A'), ord('z') + 1):
    dict1 = {}
    dict1[chr(char)] = char
    lst.append(dict1)
for i in lst:
    print(i)
