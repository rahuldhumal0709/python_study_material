from datetime import datetime,date
date_today=str(date.today())
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
upcoming_ongoing=[]
content=[{"Id":1,"Start Date":"2023-07-20","Start Time":"19:00:00"},{"Id":2,"Start Date":"2023-07-18","Start Time":"10:00:00"},{"Id":3,"Start Date":"2023-07-25","Start Time":"17:00:00"}]
for i in range(len(content)):
    if content[i]["Start Date"]>date_today:
        upcoming_ongoing.append(content[i])
    elif content[i]["Start Date"]==date_today:
        if content[i]["Start Time"]>current_time:
            upcoming_ongoing.append(content[i])
print(upcoming_ongoing)