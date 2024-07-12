# Save records of five students in list

# for i in range(5):
#     dict1 = {}
#     dict1['Name'] = input("Enter Name : ")
#     dict1['Roll No'] = input("Enter RollNo : ")
#     dict1['Math'] = input("Enter Math marks : ")
#     dict1['Physics'] = input("Enter Physics marks : ")
#     dict1['Chemistry'] = input("Enter Chemistry marks: ")
#     dict1['Biology'] = input("Enter Biology marks: ")
#     lst.append(dict1)
#     print("Record successfully saved\n")
# print(lst)
# List of student records
students = [
    {'Name': 'Dipak', 'Roll No': '48', 'Math': '85', 'Physics': '90', 'Chemistry': '88', 'Biology': '95'},
    {'Name': 'Rahul', 'Roll No': '47', 'Math': '97', 'Physics': '91', 'Chemistry': '82', 'Biology': '80'},
    {'Name': 'Shubhangi', 'Roll No': '17', 'Math': '85', 'Physics': '87', 'Chemistry': '89', 'Biology': '90'},
    {'Name': 'Apeksha', 'Roll No': '49', 'Math': '80', 'Physics': '78', 'Chemistry': '82', 'Biology': '85'},
    {'Name': 'Swapnil', 'Roll No': '50', 'Math': '82', 'Physics': '84', 'Chemistry': '95', 'Biology': '83'}
]

topper_list = []

for student in students:
    total_marks = 0
    for subject, marks in student.items():
        if subject in ['Math', 'Physics', 'Chemistry', 'Biology']:
            total_marks += int(marks)
    avg_marks = total_marks / 4
    topper_list.append({'Name': student['Name'], 'Average Marks': avg_marks})
print(topper_list)
sorted_toppers = sorted(topper_list, key=lambda x: x['Average Marks'], reverse=True)

rank = 1
for topper in sorted_toppers:
    print(f"{topper['Name']}, Rank: {rank}")
    rank += 1