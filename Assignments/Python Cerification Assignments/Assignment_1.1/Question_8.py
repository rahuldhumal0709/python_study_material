# Q8. Python program to find the largest number in a list without using built-in functions.

my_list=[]
size_of_list=int(input("Size of list : "))
for i in range(0,size_of_list):
    element=int(input())
    my_list.append(element)
print(my_list)
big = my_list[0]
position = 0
for i in range(len(my_list)):
    if (my_list[i]>big):
        big = my_list[i]
        position = i
print("The largest element is ",big," which is found at position ",position)