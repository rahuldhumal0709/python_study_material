lst = [10,20,25,30,40,45,50]
print("Original : ",lst)

lst.append(70)
print("Append : ",lst)

lst.extend([15,35,55])
print("Extend : ",lst)

lst.insert(1,13)
print("Insert : ",lst)

lst.pop()
print("Pop last item: ",lst)

lst.pop(2)
print("Pop item using index: ",lst)

lst2 = lst.copy()
print('Copy : ',lst2)

lst2.append(100)
print('lst1 : ',lst)
print('lst2 : ',lst2)

lst2.sort()
print('After sort (ascending order): ',lst2)

lst2.sort(reverse=True)
print('After sort (descending order): ',lst2)

print('Before reverse : ',lst)
lst.reverse()
print('After reverse : ',lst)

lst.remove(15)
print('Remove item : ',lst)

find_index = lst.index(13)
print('find_index_using_item: ',find_index)

lst.extend([50,70,50])
print('lst : ',lst)

item_count = lst.count(50)
print('count : ',item_count)

lst.clear()
print('Removed all items : ',lst)

lst.append(10)
print('Added new item : ',lst)