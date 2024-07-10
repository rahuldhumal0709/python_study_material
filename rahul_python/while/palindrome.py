num=int(input("Enter a number="))
num1 = num
count=0
while(num>0):
    rem =num % 10
    num =num // 10
    count =rem+(count*10)
if(count==num1):
    print("palindrome")
else:
    print("not palindrome")