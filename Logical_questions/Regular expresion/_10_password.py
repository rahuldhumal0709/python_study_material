import re
password = input("Enter your password : ")
res = re.findall(r"^.*(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]){8,16}.*$",password)
print(res)
if res:
    print("Given passsword format is correct")
else:
    print("Given password format is incorrect")