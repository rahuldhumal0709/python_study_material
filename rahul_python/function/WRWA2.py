#find factorial for With return with argument
def factWRWA(x):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact
a=int(input("enter a number="))
res=factWRWA(a)
print(res)