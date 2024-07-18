# Write a program to get input of alphabetic strings from the user, save them in a list, and print the list.
# Continue this process until the user enters a non-alphabetic string.
lst = []
print("Please enter alpha string")
while(True):
    inp_str = input()
    if inp_str.isalpha():
        lst.append(inp_str)
    else:
        print("You enterd non-alpha string")
        break
print("The final list is :",lst)