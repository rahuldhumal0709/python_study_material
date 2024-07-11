# Output :
# *
# *   *
# *   *   *
# *   *   *   *
# *   *   *   *   *

for i in range(0,5):
    for j in range(0,i+1):
        print('*',end=' ')
    print()
print()

# ==============================================
# 1
# 1   2
# 1   2   3
# 1   2   3   4
# 1   2   3   4   5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print()

# ==============================================
# 1
# 2   3
# 4   5   6
# 7   8   9   10

n = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(n,end=' ')
        n = n + 1
    print()
print()
# ==============================================
# 5   4   3   2   1
#     4   3   2   1
#         3   2   1
#             2   1
#                 1

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(i,0,-1):
        print(k,end=' ')
    print()
print()

# ==============================================
# 9   8   7   6
#     5   4   3
#         2   1
#             0

n = 9
for i in range(4,-1,-1):
    for j in range(4,i,-1):
        print(' ',end=' ')
    for k in range(i,0,-1):
        print(n,end=' ')
        n = n - 1
    print()
print()
