num=int(input("Enter 4 digit number : "))
count=0
while(num>0):
    rem = num % 10
    num = num // 10
    count=rem+(count*10)
print(count)
