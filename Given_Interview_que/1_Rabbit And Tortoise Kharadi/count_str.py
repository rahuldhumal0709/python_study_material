lst=["abc","abcd","ab","bcdgdg","c"]
dict1={i:len(i) for i in lst}
print(dict1)

#---------------------------------------------------------
str1=dict()
for i in lst:
    count=len(i)
    str1[i]=count
print(str1)

# {'abc': 3, 'abcd': 4, 'ab': 2, 'bcdgdg': 6, 'c': 1}