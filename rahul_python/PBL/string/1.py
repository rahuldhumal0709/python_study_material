# WAP to count the number of upper and lower case letters in a string.
string="Wipro Technologies"
count1=0
count2=0
for i in string:
      if(i.isupper()):
            count1=count1+1
      elif(i.islower()):
            count2=count2+1
print("The number of upper case letters is : ",count1)
print("The number of lower case letters is : ",count2)