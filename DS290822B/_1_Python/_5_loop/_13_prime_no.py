# no = int(input("Enter your no :  "))

# if no != 1:
#     for i in range(2,no):
#         if no % i == 0:
#             print("Composite no")
#             break
#     else:
#         print("Prime no")
# else:
#     print("It is neight prime nor composite")

num=int(input("Enter a number : "))
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
if flag==0:
    print("Prime number")
else:
    print("Not Prime")