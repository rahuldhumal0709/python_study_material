try:
    a=int(input("Enter a number="))
    b=int(input("Enter a number="))
    c=a//b
    print(c)
except ZeroDivisionError as e:
    print("Error:",e)
except ValueError as e1:
    print("Error:",e1)
finally:
    print("Always Executed")
print("End of program")