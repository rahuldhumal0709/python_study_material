import json

file = open("Assignments\\Assignment_6\\6_Assignment_1\\employee.json")

# convert json file into list
lst = json.load(file)
print(lst)