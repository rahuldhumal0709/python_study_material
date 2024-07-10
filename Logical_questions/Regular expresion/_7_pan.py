import re
pan=input()
res1 = re.findall("^[A-Z]{5}[0-9]{4}[A-Z]{1}$",pan)
print(res1)
if res1:
    print("Given format is correct")
else:
    print("Given format is incorrect")