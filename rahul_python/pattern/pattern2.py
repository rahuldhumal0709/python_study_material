#nested for loop.
for i in range(1,5):
    for j in range(1,6-i):
        print(j,end="\t")
    print()

# 1       2       3       4
# 1       2       3
# 1       2
# 1