# WAP to replace last value of tuples in a list to 100.
MyList=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([tup[:-1] + (100,) for tup in MyList])