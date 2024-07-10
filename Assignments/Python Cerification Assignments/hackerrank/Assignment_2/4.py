from itertools import combinations
str1,n=(input()).split()
n=int(n)
str1=list(str1)
str1.sort()
for i in range(1,n+1):
    l=list(combinations(str1,i))
    l.sort()
    for j in l:
        print(''.join(j))