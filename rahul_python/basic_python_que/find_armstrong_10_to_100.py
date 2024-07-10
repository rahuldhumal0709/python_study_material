lst=[]
count=0
for num in range(10,100000):
    num1 = num
    res=0
    order = len(str(num))
    while num1 > 0:
        rem = num1 % 10
        res = res + rem ** order
        num1 = num1 // 10
    if num == res:
        count= count+1
        lst.append(num)
print(lst)
# print(len(lst))
print(count)