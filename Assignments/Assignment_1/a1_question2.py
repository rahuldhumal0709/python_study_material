# Write a Python program that accepts a word from the user and reverse it.
str=input()
reverse_str=""
count=len(str)
while count > 0:   
    reverse_str += str[ count - 1 ]
    count = count - 1
    print(reverse_str)