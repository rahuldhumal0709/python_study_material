class addition:
    def input(self):
        self.a=int(input("Enter="))
        self.b=int(input("Enter="))
    def operation(self):
        self.c=self.a+self.b
    def output(self):
        print(self.c)
obj=addition()
obj.input()
obj.operation()
obj.output()