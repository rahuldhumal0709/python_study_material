# WAP to check if a given number is positive,negative, or zero
n=int(input("Enter a number "))
if(n>=0):
    if(n>0):
        print("Given number is positive")
    else:
        print("Given number is zero")
else:
    print("Given number is negative")