a=15
for i in range(5,0,-1):
    for k in range(i,5):
        print(end="\t")
    for j in range(i,0,-1):
        print(a,end="\t")
        a=a-1
    print()

# 15      14      13      12      11
#         10      9       8       7
#                 6       5       4
#                         3       2
#                                 1