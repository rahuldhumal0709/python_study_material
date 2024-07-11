# * String 
# --> A String is a data structure that represents a sequence of characters.
# --> It is an immutable data type.
# --> Their are various string methods in python.
# ==========================================================================
str1 = 'Python Programming'
str2 = "rahul sainath dhumal"
print(str1)
print(str2)
# ==========================================================================
# 1)lower() - Converts all character in the string to lowercase.
str_lower = str1.lower()
print('string lower : ',str_lower)
# ==========================================================================
# 2)upper() - Converts all character in the string to uppercase.
str_upper = str1.upper()
print('string upper : ',str_upper)
# ==========================================================================
# 3)capitalize() - Capitalize the first character of the string.
string_capitalize = str2.capitalize()
print('string_capitalize : ',string_capitalize)
# ==========================================================================
# 4)title() - Capitalize the first character of each word in the string.
string_title = str2.title()
print('string_title : ',string_title)
# ==========================================================================
# 5)startswith() - Check if the string starts with a specific substring.
string_startswith = str1.startswith('P')
print('string_startswith : ',string_startswith)
# ==========================================================================
# 6)endswith() - Check if the string ends with a specific substring.
string_endswith = str1.endswith('e')
print('string_endswith : ',string_endswith)
# ==========================================================================
# 7)split() - Split the string into a list of substrings bases on a delimiter.
string_split = str1.split(' ')
print('string_split : ',string_split)
# ==========================================================================
# 8)replace() - Replaces occurrences of a substring with another substring.
string_replace = str1.replace('Python','Java')
print('string_replace : ',string_replace)
# ==========================================================================
# 9)join() - Replaces occurrences of a substring with another substring.
string_join = ' '.join(['My','name','is','Rahul'])
print('string_join : ',string_join)
# ==========================================================================
# 10)find() - Find the first occurrences of a substring in the string.
string_find = str2.find('n')
print('string_find : ',string_find)
# ==========================================================================
# 11)count() - Count the occurrences of a substring in the string.
string_count = str2.count('h')
print('string_count : ',string_count)
# ==========================================================================
# 12)isalpha() - Check if all characters in the string are alphabetic.
str3 = 'rahul'
string_isalpha = str3.isalpha()
print('string_isalpha : ',string_isalpha)
# ==========================================================================
# 13)isdigit() - Check if all characters in the string are digit.
str4 = '12345'
string_isdigit = str4.isdigit()
print('string_isdigit : ',string_isdigit)
# ==========================================================================
# 14)isalnum() - Check if all characters in the string are alpha numeric.
str5 = 'rahul123'
string_isalnum = str4.isalnum()
print('string_isalnum : ',string_isalnum)
# ==========================================================================
# 15)islower() - Check if all characters in the string are lowercase.
string_islower = str1.islower()
print('string_islower : ',string_islower)
# ==========================================================================
# 16)isupper() - Check if all characters in the string are uppercase.
string_isupper = str1.isupper()
print('string_isupper : ',string_isupper)
# ==========================================================================
# 17)isspace() - Check if the string contains only white space characters.
str5 = '   '
string_isspace = str5.isspace()
print('string_isspace : ',string_isspace)
# ==========================================================================
# 18)isnumeric() - Check if all characters in the string are numeric.
str6 = '123'
string_isnumeric = str6.isnumeric()
print('string_isnumeric : ',string_isnumeric)
# ==========================================================================