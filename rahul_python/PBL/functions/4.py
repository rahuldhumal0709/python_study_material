# Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
def upperlower(s):
    count1=0
    count2=0
    for i in string:
        if(i.isupper()):
                count1=count1+1
        elif(i.islower()):
                count2=count2+1
    print("The number of upper case letters is : ",count1)
    print("The number of lower case letters is : ",count2)
string=input("Enter a string : ")
upperlower(string)