# class test:
#     def __init__(self,x='I love Edyoda'):
#         self.x=x

#     def display(self):
#         print(self.x)
# obj=test()
# obj.display()

# class Edyoda:
#     def __init__(self,batch):
#         self.batch=batch
# obj=Edyoda('Data Science')

# obj.course='Python'
# obj.hours=2
# print(obj.hours*len(obj.__dict__))

# class Demo:
#     def __init__(self):
#         pass
#     def test(self):
#         print(__name__)
# obj=Demo()
# obj.test()

class test:
    def __init__(self):
        self.variable='New'
        self.Change(self.variable)
    def Change(self,var):
        var='Old'
obj=test()
print(obj.variable)