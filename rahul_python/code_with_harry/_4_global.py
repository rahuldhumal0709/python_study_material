x = 89
def harry():
    y = 20
    def rohan():
        global z
        z = 88
        print("before calling rohan()", x)
        print("before calling rohan()", y)
        print("before calling rohan()", z)   
    rohan()
    print("after calling rohan()", x)
    print("before calling rohan()", y)
    print("before calling rohan()", z)

harry()
print(x)
print(z)
