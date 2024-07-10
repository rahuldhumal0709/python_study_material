class mobile:
    count=0
    def __init__(self):
        self.price=None
        print("inside the init_method")
        self.count=self.count+1
    def setprice(self,price):
        self.price=price
    def getprice(self):
        return self.price
    def display(self):
        print("price",self.price)
    
mob1=mobile()
mob2=mobile()
print(mobile.count)
mob1.setprice(1000) #(mob1=reference variable)
mob2.setprice(2000)
mob1.display()
mob2.display()