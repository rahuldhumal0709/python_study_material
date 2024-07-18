# 423 - take input from user
# o/p : Four Two Three

# num = int(input('Enter a number : '))
# str_num = str(num)
# d={'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
# res = [d[i] for i in str_num]
# for j in res:
#     print(j,end=' ')
# print()

lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8]

# intersection
# result = [i for i in lst1 for j in lst2 if i==j]
# print(result)

#union
# lst1.extend([j for j in lst2 if j not in lst1])
# print(lst1)

result = ["even" if n%2 == 0 else "odd" for n in range(10)]
print(result)
