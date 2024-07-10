lst = []
size=int(input("Enter the size of list : "))
for i in range(0,size):
    ele=int(input())
    lst.append(ele)
print(lst)
# lst=[5, 9, 3, 8, 1, 7, 4]
len = len(lst)
mid = len//2
for i in range(mid):
    lst[i],lst[len-i-1]=lst[len-i-1],lst[i]  #swaping
print(lst)
#---------------------------------------------------------------
# lst1 = [8,7,5,3,4,9,1,6]
# len=len(lst1)
# mid=len//2
# i=0
# while mid>i:
#     for j in range(len-1,mid-1,-1):
#         lst1[i],lst1[j]=lst1[j],lst1[i]
#         i = i+1
#     print("Reverse list : ",lst1)