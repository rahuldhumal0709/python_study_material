# Write a Python function to sum all the numbers in a list.
def addition():
    my_list=[]
    size_of_list=int(input("Size of list : "))
    for i in range(0,size_of_list):
        element=int(input())
        my_list.append(element)
    sum=0
    for i in range(0,len(my_list)):
        sum = my_list[i] + sum
    print(sum)
addition()