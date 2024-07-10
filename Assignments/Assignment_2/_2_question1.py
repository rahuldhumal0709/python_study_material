# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
i=1
for j in range(0,5):
    for k in range(j+1,5):
        if l[j][i] > l[k][i]:
            l[j],l[k]=l[k],l[j]
print(l)