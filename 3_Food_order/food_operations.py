import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def AutoGenerate_FoodID():
    #generate a random Food ID
    Food_ID=''.join(random.choices(string.digits,k=4))
    return Food_ID
#---------------------------------------------------------------------------------------------------------------Done

def Register(type,admin_json_file,user_json_file,Full_Name,Email,Password):
    '''Register the admin/user based on the type with the given details'''
    if type.lower()=='admin':
        file = open(admin_json_file,'r+')
    else:
        file = open(user_json_file,'r+')
    d={
        "Full Name":Full_Name,
        "Email":Email,
        "Password":Password
    }
    try:
        content=json.load(file)
        if d not in content:
            content.append(d)
            file.seek(0)
            file.truncate()
            json.dump(content,file)
            file.close()
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l,file)
        file.close()
#---------------------------------------------------------------------------------------------------------------Done

def Login(type,admin_json_file,user_json_file,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    temp=0
    if type.lower()=='admin':
        file = open(admin_json_file,'r')
    else:
        file = open(user_json_file,'r')
    try:
        content=json.load(file)
    except JSONDecodeError:
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            temp=1
            break
    if temp==0:
        file.close()
        return False
    file.close()
    return True
#---------------------------------------------------------------------------------------------------------------Done

def Add_Food(Admin_name,food_json_file,Food_ID,Food_Name,Food_qnt,Food_initial_price,Discount,Final_price,Total_Stock,Available_Stock,food_order_by_user,total_income,received_income,percentage_of_received_income):
    '''Add a food with the details entered by admin'''
    d={
        "Food Id":Food_ID,
        "Food Name":Food_Name,
        "Admin Name":Admin_name,
        "Food Quantity":Food_qnt,
        "Food Initial Price":Food_initial_price,
        "Discount(%)":Discount,
        "Final Price as per Qnt":Final_price,
        "Total Stock":Total_Stock,
        "Available Stock":Available_Stock,
        "Food Order By User":food_order_by_user,
        "Total Income":total_income,
        "Received Income":received_income,
        "Percentage of Received Income":percentage_of_received_income
    }
    with open(food_json_file,'r+') as file:
        try:
            content=json.load(file)
            if d not in content:
                content.append(d)
                file.seek(0)
                file.truncate()
                json.dump(content,file)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,file)
#---------------------------------------------------------------------------------------------------------------Done

def View_Foods(Admin_name,food_json_file):
    '''Return a list of all foods added by the logged in admin'''
    details=[]
    with open(food_json_file,'r') as f:
        try:
            content=json.load(f)
        except JSONDecodeError:
            return details
        for i in range(len(content)):
            if content[i]["Admin Name"]==Admin_name:
                details.append(content[i])
        return details
#---------------------------------------------------------------------------------------------------------------Done

def View_Food_Details_ByID(Admin_name,food_json_file,Food_ID):
    '''Return details of the event for the event ID entered by user'''
    Details=[]
    with open(food_json_file,'r') as f:
        content2=json.load(f)
        for i in range(len(content2)):
            if content2[i]['Admin Name']==Admin_name and content2[i]['Food Id']==Food_ID:
                Details.append(content2[i])
                break
        return Details
#---------------------------------------------------------------------------------------------------------------Done

def Update_Food(Admin_name,food_json_file,Food_ID,new_food_name,new_food_qnt,new_food_initial_price,new_discount,new_final_price_as_per_qnt,new_total_stock,available_stock,food_order_by_user,new_total_income,received_income,new_percentage_of_received_income):
    '''Update Event by ID || Take the key name to be updated from member, then update the value entered by user for that key for the selected event
    || Return True if successful else False'''
    with open(food_json_file,'r+') as f:
        content3=json.load(f)
        for i in range(len(content3)):
            if content3[i]["Admin Name"]==Admin_name and content3[i]['Food Id']==Food_ID:
                content3[i]["Food Name"]=new_food_name
                content3[i]["Food Quantity"]=new_food_qnt
                content3[i]["Food Initial Price"]=new_food_initial_price
                content3[i]["Discount(%)"]=new_discount
                content3[i]["Final Price as per Qnt"]=new_final_price_as_per_qnt
                content3[i]["Total Stock"]=new_total_stock
                content3[i]["Available Stock"]=available_stock
                content3[i]["Food Order By User"]=food_order_by_user
                content3[i]["Total Income"]=new_total_income
                content3[i]["Received Income"]=received_income
                content3[i]["Percentage of Received Income"]=new_percentage_of_received_income
                f.seek(0)
                f.truncate()
                json.dump(content3,f)
                return True
        return False
#---------------------------------------------------------------------------------------------------------------Done

def Delete_Food(Admin_name,food_json_file,Food_ID):
    '''Delete the Event with the entered Event ID || Return True if successful else False'''
    with open(food_json_file,'r+') as f:
        content4=json.load(f)
        for i in range(len(content4)):
            if content4[i]["Admin Name"]==Admin_name and content4[i]['Food Id']==Food_ID:
                del content4[i]
                f.seek(0)
                f.truncate()
                json.dump(content4,f)
                return True
        return False
#---------------------------------------------------------------------------------------------------------------Pending

def Order_Food(User_name,food_json_file,Food_ID,Mobile_No,Address,Food_Quantity,Total_Bill,received_income,percentage_of_received_income):
    '''Register the logged in member in the event with the event ID entered by member. 
    (append Full Name inside the "Users Registered" list of the selected event)) 
    Return True if successful else return False'''
    d={
        "Name":User_name,
        "Mobile No":Mobile_No,
        "Address":Address,
        "Food quantity":Food_Quantity,
        "Total Bill":Total_Bill
        }
    with open(food_json_file,"r+") as f:
        try:
            content=json.load(f)
            for i in range(len(content)):
                if content[i]["Food Id"]==Food_ID:
                    if content[i]["Available Stock"]>=Food_Quantity:
                        content[i]["Food Order By User"].append(d)
                        content[i]["Available Stock"]=content[i]["Available Stock"]-Food_Quantity
                        content[i]["Received Income"]=received_income
                        content[i]["Percentage of Received Income"]=percentage_of_received_income
                        f.seek(0)
                        f.truncate()
                        json.dump(content,f)
                        return True
        except JSONDecodeError:
            return False
        return False
#---------------------------------------------------------------------------------------------------------------Pending

def fetch_all_events(events_json_file,Full_Name,event_details,upcoming_ongoing):
    '''Append the details of all upcoming and ongoing events list based on the today's date/time and event's date/time'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open(events_json_file,"r") as f:
        content=json.load(f)
        for i in range(len(content)):
            for j in range (len(content[i]["Users Registered"])):
                if content[i]["Users Registered"][j]["Name"]==Full_Name:
                    event_details.append(content[i])
                    if content[i]["Start Date"]>date_today:
                        upcoming_ongoing.append(content[i])
                    elif content[i]["Start Date"]==date_today:
                        if content[i]["Start Time"]>=current_time:
                            upcoming_ongoing.append(content[i])
        return upcoming_ongoing
#---------------------------------------------------------------------------------------------------------------Pending

def Update_Password(members_json_file,Full_Name,new_password):
    '''Update the password of the member by taking a new passowrd || Return True if successful else return False'''
    with open(members_json_file,"r+") as f:
        content=json.load(f)
        for i in range(len(content)):
            if content[i]["Full Name"]==Full_Name:
                try:
                    a=content[i]["Password"]
                except KeyError:
                    return False
                content[i]["Password"]=new_password
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                return True
        return False
#---------------------------------------------------------------------------------------------------------------Done

def View_all_Foods(food_json_file):
    '''Read all the events created | DO NOT change this function'''
    details=[]
    with open(food_json_file,"r") as f:
        try:
            content=json.load(f)
        except JSONDecodeError:
            return details
        for i in range(len(content)):
            details.append(content[i])
        return details