# def SortStudentMarks(cls,input1,input2,input3):
        
#     n = input1
#     m = input2
#     arr = input3
#     ind = -1
#     avg = float('inf')
#     for i in range(m):
#         sum =0.0
#         for j in range(n):
#             sum += arr[j][i]
#         sum /= n
#         if avg > sum:
#             avg = sum
#             ind = i
    
#     ans = [0]*n
#     for i in range(n):
#         sum = 0
#         for j in range(m):
#             if(j == ind):
#                 continue
            
#             sum += arr[i][j]
#         ans[i] = sum
    
#     return ans
    
c=list(map(int, input().split()))
e=input()
l=int(input())
e=list(e)
#print(c)
#print(e)
count=0
for i in range(l):
    if e[i]=='N':
        count=count-c[i]
    else:
        count=count+c[i]
        
print(abs(count*100))
