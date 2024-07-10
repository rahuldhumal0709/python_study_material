class Addition:
    def inputs(self,a,b):
        self.a=a
        self.b=b
    def outputs(self):
        return self.a+self.b
a=int(input())
b=int(input())
c=Addition()
c.inputs(a,b)
res=c.outputs()
print(res)