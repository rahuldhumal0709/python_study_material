#find minimum number
from typing import Sized


a=int(input()) #758
l=[]
while(a>0):     #758>0=T    75>0=T
    n=a%10      #758%10=8   75%10=5
    a=a//10     #758//10=75 75//10=7
    l.append(n)
print("Total number of element in list = ",len(l))
print("Minimum number is = ",min(l))
print("Maximum number is = ",max(l))




