size = int(input("Enter the size of list :"))

lst = []
for i in range(size):
    element = int(input("Enter a number :"))
    lst.append(element)
print(lst)
while True:
    print("Enter 0 if you want to stop the program")
    item = int(input("Enter the item to check whether it is present inside the list or not :"))
    if item==0:
        print("Thank You")
        break
    elif item in lst:
        print(f"{item} is present in the list") 
    else:
        print(f"{item} is not present in the list")


