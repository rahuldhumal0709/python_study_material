inp=int(input())
for i in range(inp):
    for j in range(2):
        items,rupees=map(int,input().split())
        if items>2:#4>2
            res=rupees*2#8
            items=items-3#1
            if items>=1:
                res=rupees*2
                items=items-3
                if items>=1:
                    res=rupees*2
                    items=items-3
    print(res)