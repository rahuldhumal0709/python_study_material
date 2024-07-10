dict1={"A":"Book1","B":"Book2","C":"Book3"}
print("Iterate Dict Items")
for k,v in dict1.items():
    print(k,v)

print("\nIterate Dict Keys")
for k in dict1.keys():
    print(k)

print("\nIterate Dict Values")
for v in dict1.values():
    print(v)

print("\nIterate Values using key")
print(dict1["B"])