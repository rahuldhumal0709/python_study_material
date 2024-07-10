# WAP to sum all the values in a dictionary, considering the values will be of int type.
Mydic2={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
sum = 0
for i in Mydic2.values():
    sum=sum+i
print(sum)