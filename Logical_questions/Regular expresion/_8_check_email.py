import re
email = input("Enter your Email : ")
res = re.findall(r'\b[A-z][A-z0-9._]+\@[A-z]+\.[A-z]{2,}\b',email)
print(res)
if res:
    print("Given Email format is correct")
else:
    print("Given Email format is incorrect")