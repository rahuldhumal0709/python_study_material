my_string=input("Enter a string : ")
#output=KLR
ans=my_string[0]
for i in my_string[1:]:
    if i not in ans:
        ans+=i
print(ans)