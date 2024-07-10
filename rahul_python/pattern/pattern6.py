for i in range(4,0,-1):
    for k in range(i,4):
        print(end="\t")
    for j in range(i,0,-1):
        print(j,end="\t")
    print()

# 4       3       2       1
#         3       2       1
#                 2       1
#                         1