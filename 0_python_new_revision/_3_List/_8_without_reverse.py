lst = [10,20,30,40,50]
# lst = lst[::-1]
# print(lst)

mid = len(lst)//2
count=0
while mid>count:
    for j in range(len(lst)-1,mid-1,-1):
        lst[count],lst[j]=lst[j],lst[count]
        count += 1
print(lst)