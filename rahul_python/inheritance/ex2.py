class student:
    def input(self):
        self.a=input("Enter a name=")
        self.b=int(input("Enter a Roll_no="))
        self.c=int(input("Enter a English marks="))
        self.d=int(input("Enter a math marks="))
        self.e=int(input("Enter a science marks="))
        self.f=int(input("Enter a physics marks="))
class result(student):
    def output(self):
        self.total=self.c+self.d+self.e+self.f
        self.avg=self.total/4
        print("Total marks is=",self.total)
        print("average is=",self.avg)
        print(end="\n")
obj=result()
obj.input()
obj.output()