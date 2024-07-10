# Q17. Python program to calculate result of a student.

def studet_result():
    name=input("\nEnter Name : ")
    roll_no=int(input("Enter a roll no : "))
    english=int(input("Enter a English marks :"))
    math=int(input("Enter a math marks : "))
    science=int(input("Enter a science marks : "))
    physics=int(input("Enter a physics marks : "))
    total = english + math + science + physics
    print(end="\n")
    print("Name : ",name)
    print("Roll_no : ",roll_no)
    print("Total marks is : ",total)
    avg=total/4
    if avg>=90:
        print("Result is Grade A+ : % : ",avg)
    elif avg<90 and avg>=75:
        print("Result is Grade A : % : ",avg)
    elif avg<75 and avg>=60:
        print("Result is Grade B+ : % : ",avg)
    elif avg<60 and avg>=40:
        print("Result is Grade B : % : ",avg)
    else:
        print("Result is Fail : % : ",avg)
studet_result()
