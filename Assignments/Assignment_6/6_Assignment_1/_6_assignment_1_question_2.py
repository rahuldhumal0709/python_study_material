import json

dict1={"Maharashtra":"Mumbai",
"Karnataka":"Bengaluru",
"Kerala":"Thiruvananthapuram",
"Goa":"Panaji",
"Telangana":"Hyderabad",
"Jharkhand":"Ranchi",
"Bihar":"Patna"}

# convert dictionary into json file
with open("Assignments\\Assignment_6\\6_Assignment_1\\states_capitals.json", "w") as file:
    json.dump(dict1, file)