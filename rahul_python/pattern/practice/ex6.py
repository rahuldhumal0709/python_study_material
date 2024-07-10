count=0
lt = list(map(int,input().split(',')))
for i in range(0,len(lt)):
    if(lt[i]>0):
        rem = lt[i] % 10
        div = lt[i] // 10
        total =(rem*10) + div
        for j in range(0,len(lt)):
            if(total==lt[j]):
                if not(lt[i]==lt[j]):
                    print("(",total,",",lt[i],")",end=" ")
                    count=count+1
                    res=count//2
print(end="\n")
print(count)