import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def AutoGenerate_EventID():
    #generate a random Event ID
    Event_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Event_ID

def Register(type,member_json_file,organizer_json_file,Full_Name,Email,Password):
    '''Register the member/ogranizer based on the type with the given details'''
    if type.lower()=='organizer':
        f = open(organizer_json_file,'r+')
    else:
        f = open(member_json_file,'r+')
    d={
        "Full Name":Full_Name,
        "Email":Email,
        "Password":Password
    }
    try:
        content=json.load(f)
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close()
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l,f)
        f.close()

def Login(type,members_json_file,organizers_json_file,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    temp=0
    if type.lower()=='organizer':
        f = open(organizers_json_file,'r')
    else:
        f = open(members_json_file,'r')
    try:
        content=json.load(f)
    except JSONDecodeError:
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            temp=1
            break
    if temp==0:
        return False
    return True

def Create_Event(org,events_json_file,Event_ID,Event_Name,Start_Date,Start_Time,End_Date,End_Time,Users_Registered,Capacity,Availability):
    '''Create an Event with the details entered by organizer'''
    d={
        "Id":Event_ID,
        "Name":Event_Name,
        "Organizer":org,
        "Start Date":Start_Date,
        "Start Time":Start_Time,
        "End Date":End_Date,
        "End Time":End_Time,
        "Users Registered":Users_Registered,
        "Capacity":Capacity,
        "Seats Available":Availability
    }
    with open(events_json_file,'r+') as f:
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)

def View_Events(org,events_json_file):
    '''Return a list of all events created by the logged in organizer'''
    details=[]
    with open(events_json_file,'r') as f:
        try:
            content=json.load(f)
        except JSONDecodeError:
            return details
        for i in range(len(content)):
            if content[i]["Organizer"]==org:
                details.append(content[i])
        return details

def View_Event_ByID(events_json_file,Event_ID):
    '''Return details of the event for the event ID entered by user'''
    Details=[]
    with open(events_json_file,'r') as f:
        content2=json.load(f)
        for i in range(len(content2)):
            if content2[i]['Id']==Event_ID:
                Details.append(content2[i])
                break
        return Details

def Update_Event(org,events_json_file,event_id,detail_to_be_updated,updated_detail):
    '''Update Event by ID || Take the key name to be updated from member, then update the value entered by user for that key for the selected event
    || Return True if successful else False'''
    with open(events_json_file,'r+') as f:
        content3=json.load(f)
        for i in range(len(content3)):
            if content3[i]["Organizer"]==org and content3[i]['Id']==event_id:
                content3[i][detail_to_be_updated]=updated_detail
                f.seek(0)
                f.truncate()
                json.dump(content3,f)
                return True
        return False

def Delete_Event(org,events_json_file,event_ID):
    '''Delete the Event with the entered Event ID || Return True if successful else False'''
    with open(events_json_file,'r+') as f:
        content4=json.load(f)
        for i in range(len(content4)):
            if content4[i]["Id"]==event_ID and content4[i]['Organizer']==org:
                del content4[i]
                f.seek(0)
                f.truncate()
                json.dump(content4,f)
                return True
        return False

def Register_for_Event(events_json_file,event_id,Full_Name):
    '''Register the logged in member in the event with the event ID entered by member. 
    (append Full Name inside the "Users Registered" list of the selected event)) 
    Return True if successful else return False'''
    d={
        "Name":Full_Name
        }
    with open(events_json_file,"r+") as f:
        try:
            content=json.load(f)
            for i in range(len(content)):
                if content[i]["Id"]==event_id:
                    if content[i]["Seats Available"]>0:
                        if d in content[i]["Users Registered"]:
                            return False
                        elif d not in content[i]["Users Registered"]:
                            content[i]["Users Registered"].append(d)
                            content[i]["Seats Available"]=content[i]["Seats Available"]-1
                            f.seek(0)
                            f.truncate()
                            json.dump(content,f)
                            return True
        except JSONDecodeError:
            return False
        return False

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

def View_all_events(events_json_file):
    '''Read all the events created | DO NOT change this function'''
    details=[]
    with open(events_json_file,"r") as f:
        try:
            content=json.load(f)
        except JSONDecodeError:
            return details
        for i in range(len(content)):
            details.append(content[i])
        return details