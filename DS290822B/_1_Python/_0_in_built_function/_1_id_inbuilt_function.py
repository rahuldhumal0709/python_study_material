num = 10
num1=-10

print(num)
print(num1)

memory_loc = id(num)
memory_loc1 = id(num1)

print("Memory Location :",memory_loc)
print("Memory Location 1 :",memory_loc1)
# id()
# it returns the memory location of the passed variable


# int values are only immutable from -5 to 256