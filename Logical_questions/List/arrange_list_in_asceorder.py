# Program for Arrange a list in Ascending order

main_list=[33,10,-5,42,8,3,100]
new_list=[]
while len(main_list) != 0:
    res=min(main_list)
    new_list.append(res)
    main_list.remove(res)
print("In first program main list is empty,sort & tranferd all the items into new list.")
print("Main list :",main_list) #main list is empty, tranferd the items in new list.
print("New List :",new_list)
#----------------------------------------------------------------------------------
lst=[33,10,-5,42,8,3,100]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
print("\nIn second program main list is sort itself")
print(lst) #main list as it is.