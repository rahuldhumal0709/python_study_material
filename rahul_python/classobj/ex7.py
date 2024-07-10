class student:
    def __init__(self,n,r,e,m,s):
        self.a=n
        self.b=r
        self.c=e
        self.d=m
        self.e=s
        self.t=self.c+self.d+self.e
        self.p=self.t/3
    def output(self):
        print("name",self.a)
        print("Roll_no",self.b)
        print("English=",self.c)
        print("math=",self.d)
        print("Science=",self.e)
        print(self.t)
        print(self.p)
        print("Cunstructor called")

o=student("rahul",1,88,98,90)
o.output()
