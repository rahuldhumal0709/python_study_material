class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

print(MathUtils.add(5, 3))  # Output: 8

'''
Static Method :
--> The term "static" is more commonly used to describe a static method (@staticmethod), 
--> which is a method that does not access or modify class or instance variables.
--> A static method does not interact with class or instance variables:
'''