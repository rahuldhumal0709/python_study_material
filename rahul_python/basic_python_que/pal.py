#Palindrome or not
# num=int(input())
# num1 = num
# res=0
# while num1 > 0:
#    rem = num1 % 10
#    res =rem + res * 10
#    num1=num1//10    
# if num == res:
#    print("Palindrom number")
# else:
#    print("not Palindrome number")

my_str=input()
l=len(my_str)-1
res_str=""
for i in range(l,-1,-1):
    res_str += my_str[i]
print(res_str)
if res_str==my_str:
    print("String is palindrome")
else:
    print("String is not palindrome")
   