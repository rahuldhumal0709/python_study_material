# Write a program to print the count the occurrences of a substring in the string.
# output : [{'P':2},{'y':1},{'t':1},{'h':1},{'o':2},{'n':2},{'r':2},{'g':2},{'a':1},{'m':2},{'i':1}]

str1 = 'Python Programming'
lst = []
for i in str1:
    dict1 = {}
    if i not in str(lst):
        dict1[i] = str1.count(i)
        lst.append(dict1)
print(lst)