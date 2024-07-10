# size = int(input("Enter the size of items you want in your list : "))

# for i in range(size):
#     element = int(input("Enter element : "))
#     lst.append(element)

# print(lst)
#-------------------------------------------
# reverse a list
lst1 = [8,7,5,3,4,9,1,6]
# lst1.reverse()
# print("inbuild-method",lst1)
#--------------------------------------------
# lst2=[]
# for i in lst1:
#     lst2.insert(0,i)
# print(lst2)
#--------------------------------------------
len=len(lst1)
mid=len//2
count=0
while mid>count:
    for i in range(len-1,mid-1,-1):
        lst1[count],lst1[i]=lst1[i],lst1[count]
        count+=1
    print("Reverse list : ",lst1)

