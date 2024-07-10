# Q13.Python program to interchange first and last elements in a list.

def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList
     
my_list = []
size_of_list=int(input("Size of list : "))
for i in range(0,size_of_list):
    element=int(input())
    my_list.append(element)
print(my_list)
print(swapList(my_list))