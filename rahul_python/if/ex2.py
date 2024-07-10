a=int(input("Enter a number="))
b=int(input("Enter a number="))
c=int(input("Enter a number="))
if a>b:
    if c>a:
        print("c is greater",c)
    else:
        print(a,"a is greater")
else:
    if b>c:
        print("b is greater",b)
    else:
        print("c is greater",c)