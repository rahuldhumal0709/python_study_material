s = input()
n = set(s)
flag = 1
isPali = 1
l = len(s)%2
for i in n:
    if(s.count(i)%2):
        if(flag and l):
            flag = 0
        else:
            isPali = 0
            break
if(isPali):
    print("Yes")
else:
    print("No")