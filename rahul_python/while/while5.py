for num in range(1,1000):
    num1=num
    count=0
    while(num>0):
        rem = num % 10
        num = num // 10
        count=rem**3+count

    if(num1==count):
        print(num1,end="\n")