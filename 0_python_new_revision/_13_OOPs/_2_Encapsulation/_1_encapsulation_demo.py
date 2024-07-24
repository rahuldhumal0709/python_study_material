# Encapsulation
# binding attributes(variable) and behaviour(method) together into single unit
# accessing private member through public environment
# private member - cannot be accessed outside the class
class Employee:
    def __init__(self, name, salary):
        self.__name = name       # Private attribute
        self.__salary = salary   # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary with validation
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary amount")

# Creating an instance of Employee
emp = Employee("Dhiraj", 50000)

# Accessing private attributes via getter methods
print(emp.get_name())
print(emp.get_salary())

# Modifying private attributes via setter methods
emp.set_name("Dipak")
emp.set_salary(60000)
print(emp.get_name())
print(emp.get_salary())
