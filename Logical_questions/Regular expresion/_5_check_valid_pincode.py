import re
pincode=input()
res1 = re.findall("^[1-9]{1}[0-9]{5}$",pincode)
if res1:
    print("Given format is correct")
else:
    print("Given format is incorrect")