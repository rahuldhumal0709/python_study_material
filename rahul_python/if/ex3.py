a=input("Enter Name : ")
b=int(input("Enter a Roll_no : "))
c=int(input("Enter a English marks :"))
d=int(input("Enter a math marks : "))
e=int(input("Enter a science marks : "))
f=int(input("Enter a physics marks : "))
total=c+d+e+f
print(end="\n")
print("Name :- ",a)
print("Roll_no :- ",b)
print("Total marks is :- ",total)
avg=total/4
if avg>=90:
    print("Result is Grade A+ % = ",avg)
elif avg<90 and avg>=75:
    print("Result is Grade A % = ",avg)
elif avg<75 and avg>=60:
    print("Result is Grade B+ % = ",avg)
elif avg<60 and avg>=40:
    print("Result is Grade B % = ",avg)
else:
    print("Result is Fail % = ",avg)
    