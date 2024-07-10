lst=[12,15,17,30,33,25]
data=list(filter(lambda lst: lst%3==0 and lst%5==0,lst))
print(data)