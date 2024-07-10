class mobile:
    def __init__(self):
        self.price=None
        print("inside the init_method")
    def setprice(self,price):
        self.price=price
    def getprice(self):
        return self.price
    def display(self):
        print("price",self.price)
mob1=mobile()
mob2=mobile()
mob1.setprice(1000) #(mob1=reference variable)
mob1.display()
mob2.setprice(2000)
c=mob2.getprice()
#mob2.display()
print(c)