'''
Constructor : 
--> A constructor is a special method that is automatically called when an object is instantiated.
--> This constructor method is defined using the __init__ keyword.
--> It is used to initialize the attributes of the class when an object is created.
--> The __init__ method does not return any value.
--> Its purpose is purely to initialize the object's state.
'''

class A:
    def __init__(self,name,rollno):     # constructor
        self.name = name
        self.rollno = rollno
    def __str__(self):      # instance method / overridden method
        return f'Name : {self.name}\nRoll No : {self.rollno}'
obj = A('KL',1)
print(obj)

'''
--> The __str__ method is used to define a human-readable string representation of the object.
--> The method should return a string. It is not meant to print anything directly. or
--> the __str__ method should return a string rather than print it.
'''