str1 = "Python"
# o/p {"P":"p","Y":"y"}

dict_comp = {i.upper() : i.lower() for i in str1}
print(dict_comp)