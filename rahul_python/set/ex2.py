student = {"name= ":"Rahul",
            "Roll_no=":"CS3145",
            "Eng":60,
            "Math":90,
            "Sci" :70
 }
print(student)
for x, y in student.items():
    print(x,y)
a=student.get("Eng")
b=student.get("Math")
c=student.get("Sci")
d=a+b+c
print(d)

