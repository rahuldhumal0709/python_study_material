no = int(input("Please enter the required size of list: "))

lst1 = []

for i in range(1, no + 1):
    element = int(input("Enter Elements :"))
    lst1.append(element)

print(lst1)

for i in range(no):
    for j in range(i + 1, no): 
        if lst1[i] > lst1[j]:    
            lst1[i],lst1[j] = lst1[j],lst1[i]
print("The list with ascending order is : ", lst1)

# for i in range(len):
#     for j in range(i+1,len):
#         if lst[i]<lst[j]:
#             lst[i],lst[j]=lst[j],lst[i]
# print("sorting list items in descending order :",lst)


