# WAP to iterate over dictionary Mydic1 using for loop and print the keys alone, values alone and both keys and values.
Mydic1={0:10, 1:20, 2:30}
print("Keys")
for k in Mydic1:
    print(k)
print("Values")
for k in Mydic1:
    print(Mydic1[k])
print("Keys Values")
for key, value in Mydic1.items():
    print(key,"    ", value)