# from json.decoder import JSONDecodeError
import operations
import json
from json import JSONDecodeError

print("Welcome to Event Management app")
with open('organizers.json','r+') as file:
    try:
        content=json.load(file)
        if 'admin@gmail.com' not in str(content):
            operations.Register('organizer','members.json','organizers.json','admin','admin@gmail.com','admin')
    except JSONDecodeError:
        operations.Register('organizer','members.json','organizers.json','admin','admin@gmail.com','admin')
# c=1
while True:
    print("Press:")
    print("1: Register")
    print("2: Login")
    print("0: Exit")
    try:
        choice=int(input())
    except ValueError:
        print("Please enter valid choice")
        continue
    if choice==1:
        print("Press :")
        print("1: Register as Organizer")
        print("2: Register as Member")
        try:
            choice1=int(input())
        except ValueError:
            print("Please enter valid choice")
        if choice1==1:
            print("Enter Full Name:")
            Full_name=input()
            print("Enter Email:")
            Email=input()
            print("Enter Password:")
            Password=input()
            if (len(Full_name)*len(Email)*len(Password))==0 and '@' not in Email and '.com' not in Email:
                print("Please enter valid data")
                continue
            else:
                operations.Register('organizer','members.json','organizers.json',Full_name,Email,Password)
                print("Registered successfully as Organizer")
        elif choice1==2:
            print("Enter Full Name:")
            Full_name=input()
            print("Enter Email:")
            Email=input()
            print("Enter Password:")
            Password=input()
            if (len(Full_name)*len(Email)*len(Password))==0 and '@' not in Email and '.com' not in Email:
                print("Please enter valid data")
                continue
            else:
                operations.Register('member','members.json','organizers.json',Full_name,Email,Password)
                print("Registered successfully as Member")
        else:
            print("Please enter valid choice!")
    elif choice==2:
        print("Press: ")
        print("1: Login as Organizer")
        print("2: Login as Member")
        try:
            choice2=int(input())
        except ValueError:
            print("Please enter valid choice")
        if choice2==1:
            print("Enter Email:")
            Email=input()
            print("Enter Password:")
            Password=input()
            organizer_login_details=operations.Login('organizer','members.json','organizers.json',Email,Password)
            if organizer_login_details==False:
                print("Invalid Credentials")
                continue
            else:
                with open('organizers.json','r') as file2:
                    content2=json.load(file2)
                    org_name=""
                    for i in range(len(content2)):
                        if content2[i]["Email"]==Email and content2[i]["Password"]==Password:
                            org_name=content2[i]["Full Name"]
                            break
                    print("Welcome "+str(org_name))
                while True:
                    print("Press :")
                    print("1: Create Event")
                    print("2: View all Events created")
                    print("3: View Event Details by ID")
                    print("4: Update Event")
                    print("5: Delete Event")
                    print("0: Logout")
                    try:
                        choice3=int(input())
                    except ValueError:
                        print("Please enter valid choice")
                    if choice3==1:
                        Ev_ID=operations.AutoGenerate_EventID()
                        print("Event ID Generated - "+str(Ev_ID))
                        print("Enter Event Name:")
                        Ev_Name=input()
                        print("Enter Start Date (YYYY-MM-DD):")
                        St_dt=input()
                        print("Enter Start Time (HH:MM:SS):")
                        St_t=input()
                        print("Enter End Date (YYYY-MM-DD):")
                        En_dt=input()
                        print("Enter End Time (HH:MM:SS):")
                        En_t=input()
                        print("Enter Total Seats:")
                        try:
                            Cap=int(input())
                        except ValueError:
                            print("Please enter valid data")
                            continue
                        if (len(Ev_Name)*len(Ev_ID)*len(St_dt)*len(En_dt)*len(str(Cap)))==0 or len(St_dt)!=10 or len(En_dt)!=10 or len(St_t)!=8 or len(En_t)!=8 or St_dt>En_dt or (St_dt==En_dt and St_t>En_t):
                            print("Please enter valid data")
                            continue
                        else:
                            operations.Create_Event(org_name,'events.json',Ev_ID,Ev_Name,St_dt,St_t,En_dt,En_t,[],Cap,Cap)
                            print("Event created successfully")
                    elif choice3==2:
                        ev_details=operations.View_Events(org_name,'events.json')
                        if len(ev_details)==0:
                            print("No Events created yet! \n")
                        else:
                            for i in range(len(ev_details)):
                                print("Event ID: "+str(ev_details[i]['Id']))
                                print("Event Name: " +str(ev_details[i]['Name']))
                                print("Organizer: " +str(ev_details[i]['Organizer']))
                                print("Start Date: " +str(ev_details[i]['Start Date']))
                                print("Start Time: " +str(ev_details[i]['Start Time']))
                                print("End Date: " +str(ev_details[i]['End Date']))
                                print("End Time: " +str(ev_details[i]['End Time']))
                                print("Total Users Registered: "+str(len(ev_details[i]["Users Registered"])))
                                print("Seats Available: "+str(ev_details[i]['Seats Available']))
                                print('\n')
                    elif choice3==3:
                        print("Enter Event ID")
                        ev_id=input()
                        with open('events.json','r') as file3:
                            try:
                                content3=str(json.load(file3))
                                if ev_id not in content3:
                                    print("Invalid event ID")
                                    continue
                            except JSONDecodeError:
                                print("Events not available")
                                continue
                        ev_details_by_id=operations.View_Event_ByID('events.json',ev_id)
                        print("Event Name: " +str(ev_details_by_id[0]['Name']))
                        print("Organizer: " +str(ev_details_by_id[0]['Organizer']))
                        print("Start Date: " +str(ev_details_by_id[0]['Start Date']))
                        print("Start Time: " +str(ev_details_by_id[0]['Start Time']))
                        print("End Date: " +str(ev_details_by_id[0]['End Date']))
                        print("End Time: " +str(ev_details_by_id[0]['End Time']))
                        print("Total Seats: "+str(ev_details_by_id[0]["Capacity"]))
                        print("Seats Available: "+str(ev_details_by_id[0]['Seats Available']))
                        print('\n')
                    elif choice3==4:
                        print("Enter Event ID:")
                        ev_id=input()
                        print("Enter detail to be Updated ( Name || Start Date || Start Time || End Time || End Date ): ")
                        dtl=input()
                        print("Enter new value:")
                        updtl=input()
                        with open('events.json','r') as file4:
                            try:
                                content4=str(json.load(file4))
                            except JSONDecodeError:
                                print("No events created")
                                continue
                        if ev_id not in content4:
                            print("Invalid event ID")
                            continue
                        if (len(ev_id)*len(dtl)*len(updtl))==0:
                            print("Please enter valid data")
                            continue
                        else:
                            update_details=operations.Update_Event(org_name,'events.json',ev_id,dtl,updtl)
                        if update_details==False:
                            print("Cannot update event")
                        else:
                            print("Event updated successfully")
                    elif choice3==5:
                        print("Enter Event ID")
                        event_id=input()
                        with open('events.json','r+') as file5:
                            try:
                                content5=str(json.load(file5))
                            except JSONDecodeError:
                                print("No events created")
                                continue
                        if event_id not in content5:
                            print("Invalid event ID")
                            continue
                        if len(event_id)==0:
                            print("Please enter valid data")
                            continue
                        else:
                            delete_details=operations.Delete_Event(org_name,'events.json',event_id)
                        if delete_details==True:
                            print("Event deleted successfully")
                        else:
                            print("Cannot delete event")
                    elif choice3==0:
                        break
                    else:
                        print("Ivalid Option")
        elif choice2==2:
            print("Enter Email:")
            Email=input()
            print("Enter Password:")
            Password=input()
            member_login_details=operations.Login('member','members.json','organizers.json',Email,Password)
            if member_login_details==False:
                print("Invalid Credentials")
                continue
            else:
                with open('members.json','r') as file6:
                    content6=json.load(file6)
                    member_name=""
                    for i in range(len(content6)):
                        if content6[i]["Email"]==Email and content6[i]["Password"]==Password:
                            member_name=content6[i]["Full Name"]
                            break
                print("Welcome "+str(member_name))
                while True:
                    print("Press:")
                    print("1: View Registered Events")
                    print("2: Register for an Event")
                    print("3: Update Password")
                    print("4: View Event Details by ID")
                    print("0: Logout")
                    try:
                        choice4=int(input())
                    except ValueError:
                        print("Please enter valid choice")
                    if choice4==1:
                        all_events=[]
                        upcoming_ongoing=[]
                        fetch_details=operations.fetch_all_events('events.json',member_name,all_events,upcoming_ongoing)
                        if fetch_details:
                            print("All Upcoming/Ongoing Events: ")
                            for i in range(len(upcoming_ongoing)):
                                print("Event ID: " +str(upcoming_ongoing[i]['Id']))
                                print("Event Name: " +str(upcoming_ongoing[i]['Name']))
                                print("Start Date: " +str(upcoming_ongoing[i]['Start Date']))
                                print("Start Time: " +str(upcoming_ongoing[i]['Start Time']))
                                print("End Date: " +str(upcoming_ongoing[i]['End Date']))
                                print("End Time: " +str(upcoming_ongoing[i]['End Time']))
                                print("Organizer: " +str(upcoming_ongoing[i]['Organizer']))
                                print('\n')
                        else:
                            print("No Upcoming/Ongoing Registered Events")
                    elif choice4==2:
                        view_details=operations.View_all_events('events.json')
                        if len(view_details)==0:
                            print("No events available")
                        else:
                            print("All Events: ")
                            for i in range(len(view_details)):
                                # view=view_details[i]
                                print("Event ID: "+str(view_details[i]['Id']))
                                print("Event Name: " +str(view_details[i]['Name']))
                                print("Organizer: "+str(view_details[i]['Organizer']))
                                print("Start Date: " +str(view_details[i]['Start Date']))
                                print("Start Time: " +str(view_details[i]['Start Time']))
                                print("End Date: " +str(view_details[i]['End Date']))
                                print("End Time: " +str(view_details[i]['End Time']))
                                print("Seats Available: "+str(view_details[i]['Seats Available']))
                                print("Total Seats: "+str(view_details[i]['Capacity']))
                                print('\n')
                        print("Enter Event ID: ")
                        event_ID=input()
                        register_event=operations.Register_for_Event('events.json',event_ID,member_name)
                        with open('events.json','r') as file7:
                            content7=str(json.load(file7))
                            if event_ID not in content7:
                                print("Invalid Event ID")
                            else:
                                if register_event==True:
                                    print("Successfully Registered")
                                else:
                                    print("User has already registed for this event OR Event seats are full \n")
                    elif choice4==3:
                        print("Enter new password")
                        password=input()
                        if(len(password))<4:
                            print("Please enter valid data")
                            continue
                        update_password=operations.Update_Password('members.json',member_name,password)
                        if update_password==True:
                            print("Password updated successfully")
                        else:
                            print("Cannot update password")
                    elif choice4==4:
                        print("Enter Event ID")
                        ev_id=input()
                        with open('events.json','r') as file8:
                            try:
                                content8=str(json.load(file8))
                                if ev_id not in content8:
                                    print("Invalid event ID")
                                    continue
                            except JSONDecodeError:
                                print("Events not available")
                                continue
                        view_events_by_id=operations.View_Event_ByID('events.json',ev_id)
                        print("Event Name: " +str(view_events_by_id[0]['Name']))
                        print("Start Date: " +str(view_events_by_id[0]['Start Date']))
                        print("Start Time: " +str(view_events_by_id[0]['Start Time']))
                        print("End Date: " +str(view_events_by_id[0]['End Date']))
                        print("End Time: " +str(view_events_by_id[0]['End Time']))
                        print("End Time: " +str(view_events_by_id[0]['End Time']))
                        print("Organizer: "+str(view_events_by_id[0]["Organizer"]))
                        print("Seats Available: "+str(view_events_by_id[0]['Seats Available']))
                        print('\n')
                    elif choice4==0:
                        break
                    else:
                        print("Invalid Choice, Please enter again")
                        continue
    elif choice==0:
        break
    else:
        print("Invalid Choice, Please enter again")
        continue