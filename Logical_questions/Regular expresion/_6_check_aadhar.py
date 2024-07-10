import re
aadhar=input()
res1 = re.findall("^[1-9]{1}[0-9]{3}[-]{1}[0-9]{4}[-]{1}[0-9]{4}$",aadhar)
print(res1)
if res1:
    print("Given format is correct")
else:
    print("Given format is incorrect")