str1="Python is a programming language"
lst=str1.split(" ")
count=0
print(lst)
for i in lst:
    if len(i) > count:
        count = len(i)
        result=i
    print(result)