class A:
    def hello(self):
        print("Base class function")
class B(A):
    def hi(self):
        print("Derived class")
obj=B()
obj.hello()
obj.hi()