str1 = "Bharati" #- take input from user
# o/p : [a,i]
#---------------------------------------------------Normal way
# str1 = input("Enter a string : ")
vowels =['A','a','E','e','I','i','O','o','U','u']
s=set()
for i in str1:
    if i in vowels:
        s.add(i)
lst=list(s)
print(lst)
#--------------------------------------------------set comprehension
# str1 = input("Enter a string : ")
vowels =['A','a','E','e','I','i','O','o','U','u']
data={i for i in str1 if i in vowels}
lst=list(data)
print(lst)