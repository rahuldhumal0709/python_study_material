class A:
    name = 'KL'
    @classmethod
    def get_name(cls):
        return cls.name

    @classmethod
    def set_name(cls,name):
        cls.name = name

data = A.get_name()
print('Initial : ',data)
A.set_name("Rahul")
data = A.get_name()
print('After update : ',data)
del data        # delete object
print('After delete : ',data)
# =======================================================

'''
Class vs. Instance Methods:

Class Methods: 
--> Operate on class-level data.
--> They receive the class (cls) as the first parameter, and changes affect all instances of the class.

Instance Methods: 
--> Operate on instance-level data.
--> They receive the instance (self) as the first parameter and only affect the specific instance.
'''