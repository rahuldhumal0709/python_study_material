# sorting list in ascending order without using inbuild function.
size=int(input("Enter the size of list : "))
lst=[]
for i in range(0,size):
    ele=int(input())
    lst.append(ele)
print(lst)
# [30, 40, 10, 50, 20]
temp=0
for i in range(0,size):
    for j in range(i+1,size):
        if lst[i] > lst[j]: 

            lst[i],lst[j]=lst[j],lst[i]  #swaping
            
print(lst)