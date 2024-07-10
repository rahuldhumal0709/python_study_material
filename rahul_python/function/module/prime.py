def primeNRNA():
    flag=0
    a=int(input("Enter a number="))
    for i in range(2,a):
        if a%i==0:
            flag=1
    if (flag==0):
        print(a,"is a prime number")
    else:
        print(a,"is a not prime number") 
#primeNRNA()