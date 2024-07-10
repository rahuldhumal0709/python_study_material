# Leap year or not 
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

# def is_leap(year):
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# year = int(input())
# print(is_leap(year))
