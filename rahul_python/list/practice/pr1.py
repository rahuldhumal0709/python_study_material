#Initialize array     
arr = [5, 2, 8,8, 7, 1]
#arr.sort()
# arr.sort(reverse=True)
# print(arr)
temp = 0
# #Displaying elements of original array    
print("Elements of original array: ")  
for i in range(0, len(arr)):    
    print(arr[i], end=" ")   
print()
#Sort the array in discending order    
for i in range(0, len(arr)):    # i=0<6
    for j in range(i+1, len(arr)):    # j=1<6,2<6
        if(arr[i] < arr[j]):    # 5<2 F,5<8 T,5<8 T,
            temp = arr[i]    # temp=5,
            arr[i] = arr[j]    # arr[0]=8
            arr[j] = temp   # arr[2]=5

#Displaying elements of the array after sorting    
    
print("Elements of array sorted in discending order: ")    
for i in range(0, len(arr)):    
    print(arr[i], end=" ")