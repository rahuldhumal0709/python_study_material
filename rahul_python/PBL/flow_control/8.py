# WAP to print the sum of the digits of a given numbers.
num=int(input("Enter a number :"))
sum=0
while(num>0):
    rem=num%10
    num=num//10
    sum=sum+rem
print(sum)