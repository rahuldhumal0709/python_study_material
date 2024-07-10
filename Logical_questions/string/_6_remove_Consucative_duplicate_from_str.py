my_string="KKLRRLKR"
#output - KLRLKR
temp=my_string[0]
answer=my_string[0]
for i in my_string [1:]:
    if i != temp:
        answer+=i
        temp=i
print(answer)