#find factorial for With return No argument
def factWRNA():
    a=int(input("enter a number="))
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact
res=factWRNA()
print(res)