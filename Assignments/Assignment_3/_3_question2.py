# Write a Python program to reverse a string.
def reverse():
    str=input()
    reverse_str=""
    count=len(str)
    while count > 0:   
        reverse_str += str[ count - 1 ]
        count = count - 1
    print(reverse_str)
reverse()