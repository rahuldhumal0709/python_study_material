# Q9. Python program to implement linear search

my_list=[]
size_of_list=int(input("Size of list : "))
for i in range(0,size_of_list):
    element=int(input())
    my_list.append(element)
print(my_list)
flag = 0
x = int(input("Enter the number to be found out: "))
for i in range(len(my_list)):
    if (x==my_list[i]):
        print("Successful search, the element is found at position", i)
        flag = 1
        break
if(flag==0):
    print("Oops! Search unsuccessful")