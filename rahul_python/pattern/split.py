ip=input() #10,12,15,18,24,29,35

weights = [int(x) for x in ip.split(',')]
summ = sum(weights)
print(summ)
#143
#---------------------------------------------
arr = list(map(int,ip.strip().split(',')))
print(arr)
# [10, 12, 15, 18, 24, 29, 35]
#---------------------------------------------
l = list(map(int,ip.split(',')))
lp = len(l)-1
for i in range(len(l)-1,-1,-1):
    # if not(l[i]%5):
    for j in range(i,lp):
        l[j] = l[j]+l[j+1]
        l[j+1] = l[j] - l[j+1]
        l[j] = l[j] - l[j+1]
    lp -= 1
print(l)
# [10, 12, 15, 18, 24, 29, 35]