# Write a function to return the reverse of a string.
def reversestring(s):
    str = ""
    for i in s:
        str = i + str
    return str
alpha = input("Enter a string: ")
print(reversestring(alpha))