# it is use to initialize instance variable - hold

class student:
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
        
    def __str__(self):
        return f"Name : {self.name} \nRoll No : {self.rno}"

student_obj = student("Bharati",20)
print(student_obj)

student_obj1 = student("Vishal",30)
print(student_obj1)
