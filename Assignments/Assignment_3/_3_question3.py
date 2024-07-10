# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def letters():
    my_string=input()
    count_upper=0
    count_lower=0
    for i in my_string:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
        else:
            continue
    print("No. of Upper case characters : ",count_upper)
    print("No. of Lower case characters : ",count_lower)
letters()