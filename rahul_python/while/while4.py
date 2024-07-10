num=int(input("Enter 4 digit number : "))
num1=num
count=0
while(num>0):
    rem = num % 10
    num = num // 10
    count=(rem*rem*rem)+count
print(count)
if(num1==count):
    print(num1,"is Armstrong")
else:
    print(num1,"is not Armstrong")
