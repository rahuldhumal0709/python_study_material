tup = (10,20,30,40,50)

# This creates a generator expression, not a tuple comprehension
result = (i for i in tup if i>25)

# To see the values, you can convert the generator to a tuple
print(tuple(result))