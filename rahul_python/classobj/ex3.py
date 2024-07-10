class factorial:
    def input(self):
        self.fact=1
        self.a=int(input("enter a number="))
    def operation(self):
        for i in range(1,self.a+1):
            self.fact=self.fact*i
    def output(self):
        print(self.fact)
obj=factorial()
obj.input()
obj.operation()
obj.output()