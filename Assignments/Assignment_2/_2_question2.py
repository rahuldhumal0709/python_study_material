# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values.
d = dict()
for i in range(97,123):
    d[chr(i)] = str(i)
print(d)