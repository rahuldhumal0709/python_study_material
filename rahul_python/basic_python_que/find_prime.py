num1=int(input())
num2=int(input())
print("Prime numbers between",num1,"to",num2,"are :")
for num in range(num1,num2+1):
   if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
               break
        else:
            print(num)