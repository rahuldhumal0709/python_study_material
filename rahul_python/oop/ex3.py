class example:
    def __init__(self):
        self.__num = 10
    def get__num(self,num):
        self.__num=num
    def __change__num(self):
        self.__num=5
        return self.__num
obj=example()
obj.set__num(10)
print(obj.change__num())
