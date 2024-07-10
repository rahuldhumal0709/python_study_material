class Student:
    __name = ""
    __rollNumber = ""

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self,rollNumber):
        self.__rollNumber = rollNumber
    def getRollNumber(self):
        return self.__rollNumber
name = input("Enter name: ")
rollNumber = input("Enter rollNumber: ")
obj=Student()
obj.setName(name)
print(obj.getName())
obj.setRollNumber(rollNumber)
print(obj.getRollNumber())