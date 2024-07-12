rno = [1,2,3]
name = ["Ram","Laxman","Sita"]

zip_items = zip(rno,name)

dict1 = dict(zip_items)
print(dict1)

for k,v in dict1.items():
    print(k,v)