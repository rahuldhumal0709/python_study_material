# class -  student
# constructor

# info()
# name,rno - take input

# marks()
# maths,science,eng - take input

# percentage()
# calculate percentage

# grade()
# calculate grade

# __str__()
# college name
# name
# rno
# sci marks
# maths marks
# eng marks
# total marks / out marks
# percentage
# grade
class student:
    college_name="CSMSS"

    def info(self):
        self.name=input("Enter Your Name : ")
        self.rno=int(input("Enter Your Roll No : "))
    def marks(self):
        self.maths=int(input("Enter your Maths marks : "))
        self.science=int(input("Enter your Science marks : "))
        self.english=int(input("Enter your English marks : "))
        self.total=self.maths + self.science + self.english
    def percentage(self):
        self.per=(self.total/300)*100
    def grade(self):
        if self.per>=90:
            return 'Grade : A+'
        elif self.per>=75 and self.per<90:
            return 'Grade : A'
        elif self.per>=60 and self.per<75:
                    return 'Grade : B'
        elif self.per>=40 and self.per<60:
            return 'Grade : C'
        elif self.per<40:
            return 'Fail'
    def __str__(self):
        return f"\nCollege Name : {student.college_name} \nName : {self.name} \nRoll no : {self.rno} \nMath Marks : {self.maths} \nScience Marks : {self.science} \nEnglish Marks: {self.english} \nTotal Marks : {self.total}/300 \nPercentage : {self.per}"
obj=student()
obj.info()
obj.marks()
obj.percentage()
print(obj)
print(obj.grade())