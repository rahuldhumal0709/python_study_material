#Armstrong or not
num=int(input()) #153
order = len(str(num)) # 3
print(order)
num1 = num
res=0
while num1 > 0: # 153>0,15>0,1>0, 0>0=False
   rem = num1 % 10 # 153%10=3, 15%10=5, 1%10=1
   res =res + rem ** order # 0+27=27, 27+125=152, 152+1=153
   num1=num1//10 # 15,1,0
print(res) # 153
if num == res: #153==153
   print("Armstrong number")  #print
else:
   print("not an Armstrong number")