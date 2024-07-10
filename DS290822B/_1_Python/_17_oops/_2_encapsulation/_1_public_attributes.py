# Encapsulation
# binding attributes(variable) and behaviour(method) together into single unit
# accessing private member through public environment

# private member - cannot be accessed outside the class
class laptop:

    def __init__(self,processor,brand):
        self.__ram = "8"
        self.processor = processor
        self.brand = brand

    # setter and getter - you can specifically modify each variable
    # def set_ram(self,__ram):
    #     self.ram = __ram

    # def get_ram(self):
    #     return self.__ram

    def display(self):
        return f"Ram : {self.__ram} \nProcessor : {self.processor} \nBrand : {self.brand}"

laptop_obj = laptop("i3","HP")
print(laptop_obj.display())

# laptop_obj.set_ram("8")
# print(laptop_obj.get_ram())

# laptop_obj.set_brand("Lenovo")

# print(laptop_obj.display())