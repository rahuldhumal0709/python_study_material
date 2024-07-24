'''
--> static and class variable are same thing
--> but static method and class method are different
'''

class A:
    name = 'KL'     # class/static variable
    def __str__(self):
        return f"Name : {A.name}"
obj = A()
print(obj)