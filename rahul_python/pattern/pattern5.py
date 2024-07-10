for i in range(4,0,-1):
    for k in range(1,i):
        print(end="\t")
    for j in range(4,i-1,-1):
        print(j,end="\t")
    print()
print()

#                         4
#                 4       3
#         4       3       2
# 4       3       2       1
#------------------------------------------------------
for i in range(1,5):
    for k in range(1,i):
        print(end="\t")
    for j in range(4,i-1,-1):
        print(j,end="\t")
    print()

# 4       3       2       1
#         4       3       2
#                 4       3
#                         4
