class student:
    def input(self):
        self.a=input("Enter a name=")
        self.b=int(input("Enter a Roll_no="))
        self.c=int(input("Enter a English marks="))
        self.d=int(input("Enter a math marks="))
        self.e=int(input("Enter a science marks="))
        self.f=int(input("Enter a physics marks="))
    def operation(self):
        self.total=self.c+self.d+self.e+self.f
        self.avg=self.total/4
    def output(self):
       print("Total marks is=",self.total)
       print("average is=",self.avg)
       print(end="\n")
o=student()
b=student()
j=student()
l=[o,b,j]
for i in range (len(l)):
    l[i].input()
    l[i].operation()
    l[i].output()