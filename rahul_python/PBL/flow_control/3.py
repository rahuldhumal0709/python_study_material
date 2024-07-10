# WAP to given two non-negative values,print true if last digit in both the numbers are the same
n1=int(input("Enter a number "))
n2=int(input("Enter a number "))
res1=n1%10
res2=n2%10
if(res1==res2):
    print("true")
else:
    print("false")