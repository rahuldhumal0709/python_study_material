lst=["Rahul","Rohit","Virat","Surya","Pant"]
lst1=[]
for i in lst:
    if i.endswith('T') or i.endswith('t'):
        lst1.append(i)
print("Letter endswith T and t in given List : ",lst1)

# lst=["Rahul","Rohit","Virat","Surya","Pant"]
lst1=[]
for i in lst:
    if i.startswith('R') or i.startswith('r'):
        lst1.append(i)
print("Letter startswith R and r in given List : ",lst1)