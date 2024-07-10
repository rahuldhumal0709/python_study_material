class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        squre = self.x**2 + self.y**2 + self.z**2
        return squre
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))
obj=Point(num1,num2,num3)
print(obj.sqSum())