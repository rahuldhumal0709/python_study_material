n1=int(input("Enter 1st number : "))
n2=int(input("Enter 2nd number : "))
operation = input("Which operation you perform : ")
if n1==45 and operation == "*" and n2 == 3:
    print("555")
elif n1==56 and operation == "+" and n2 == 9:
    print("77")
elif n1==56 and operation == "/" and n2 == 6:
    print("4")
else:
    if operation=="+":
        print(n1+n2)
    elif operation=="-":
        print(n1-n2)
    elif operation=="*":
        print(n1*n2)
    elif operation=="/":
        print(n1/n2)
    elif operation=="%":
        print(n1%n2)
    else:
        print("Please enter correct arithmatic operator")