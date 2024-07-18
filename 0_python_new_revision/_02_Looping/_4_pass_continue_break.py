#pass
i=1
while(i<=10):
    if(i==5):
        pass
    else:
        print(i,end=' ')
    i = i + 1
print()
# ==============================================
#continue
for i in range(1,11):
    if(i==5):
        continue
    else:
        print(i,end=' ')
print()
# ==============================================
#break
for i in range(1,11):
    if(i==5):
        break
    print(i,end=' ')
print()
# ==============================================