# Q5.Python program to check whether given year is leap year or not.

year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("leap year")
       else:
           print("Not leap year")
   else:
       print("leap year")
else:
   print("Not leap year")