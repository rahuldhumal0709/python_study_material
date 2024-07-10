A=65
a = 97
print("Letter\t","   Ascii Value |","   Letter\t","   Ascii Value")
for i in range(1, 27):
    print("%c" %(A),"\t-\t",A,end="\t|\t")
    A +=1
    print("%c" %(a),"\t-\t",a)
    a +=1
print()