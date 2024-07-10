# from json.decoder import JSONDecodeError
import food_operations
import json
from json import JSONDecodeError

print("Welcome to Food Ordering app")
with open('admin.json','r+') as file:
    try:
        content=json.load(file)
        if 'admin@gmail.com' not in str(content):
            food_operations.Register('admin','user.json','admin.json','admin','admin@gmail.com','admin')
    except JSONDecodeError:
        food_operations.Register('admin','admin.json','user.json','admin','admin@gmail.com','admin')
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
#----------------------------------------------------------------------------------------------------------------------------------
    if choice==1:
        print("Press :")
        print("1: Register as Admin")
        print("2: Register as User")
        try:
            choice1=int(input())
        except ValueError:
            print("Please enter valid choice")
#----------------------------------------------------------------------------------------------------------------------------------Done
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
                food_operations.Register('admin','admin.json','user.json',Full_name,Email,Password)
                print("Registered successfully as Admin")
#----------------------------------------------------------------------------------------------------------------------------------Done
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
                food_operations.Register('user','admin.json','user.json',Full_name,Email,Password)
                print("Registered successfully as User")
        else:
            print("Please enter valid choice!")
#----------------------------------------------------------------------------------------------------------------------------------
    elif choice==2:
        print("Press: ")
        print("1: Login as Admin")
        print("2: Login as User")
        try:
            choice2=int(input())
        except ValueError:
            print("Please enter valid choice")
#----------------------------------------------------------------------------------------------------------------------------------Done
        if choice2==1:
            print("Enter Email:")
            Email=input()
            print("Enter Password:")
            Password=input()
            admin_login_details=food_operations.Login('admin','admin.json','user.json',Email,Password)
            if admin_login_details==False:
                print("Invalid Credentials")
                continue
            else:
                with open('admin.json','r') as file2:
                    content2=json.load(file2)
                    admin_name=""
                    for i in range(len(content2)):
                        if content2[i]["Email"]==Email and content2[i]["Password"]==Password:
                            admin_name=content2[i]["Full Name"]
                            break
                    print("Welcome "+str(admin_name))
                while True:
                    print("Press :")
                    print("1: Add Foods")
                    print("2: View all Foods")
                    print("3: View food details by ID")
                    print("4: Update Food")
                    print("5: Delete Food")
                    print("0: Logout")
                    try:
                        choice3=int(input())
                    except ValueError:
                        print("Please enter valid choice")
#----------------------------------------------------------------------------------------------------------------------------------Done
                    if choice3==1:
                        food_ID=food_operations.AutoGenerate_FoodID()
                        print("Event ID Generated - "+str(food_ID))
                        print("Enter Food Name:")
                        food_name=input()
                        try:
                            print("Enter Food Quantity : ")
                            food_qnt=int(input())
                            print("Enter Total Stock : ")
                            total_stock=int(input())
                            print("Enter Food Price(RS) : ")
                            food_initial_price=float(input())
                            print("Discount(%) : ")
                            discount=float(input())
                            final_price_as_per_qnt=food_initial_price-(food_initial_price*(discount/100))
                            print("Final price of Food as per Qnt(RS) : ",final_price_as_per_qnt)
                            food_order_by_user=[]
                            total_income=(total_stock/food_qnt)*final_price_as_per_qnt
                            total=0
                            for i in range(len(food_order_by_user)):
                                total=total+food_order_by_user[i]["Total Bill"]
                            received_income=total
                            percentage_of_received_income=(received_income/total_income)*100
                        except ValueError:
                            print("Please enter valid data")
                            continue
                        if (len(food_name)*len(food_ID)*len(str(food_qnt))*len(str(total_stock))*len(str(food_initial_price))*len(str(discount))==0) and discount>100:
                            print("Please enter valid data")
                            continue
                        else:
                            food_operations.Add_Food(admin_name,'food.json',food_ID,food_name,food_qnt,food_initial_price,discount,final_price_as_per_qnt,total_stock,total_stock,food_order_by_user,total_income,received_income,percentage_of_received_income)
                            print("Food added successfully")
#----------------------------------------------------------------------------------------------------------------------------------Done
                    elif choice3==2:
                        food_details=food_operations.View_Foods(admin_name,'food.json')
                        if len(food_details)==0:
                            print("No Foods added yet! \n")
                        else:
                            for i in range(len(food_details)):
                                print("Food ID: "+str(food_details[i]['Food Id']))
                                print("Food Name: " +str(food_details[i]['Food Name']))
                                print("Food Quantity: " +str(food_details[i]['Food Quantity']))
                                print("Food Initial Price: " +str(food_details[i]['Food Initial Price']))
                                print("Discount(%): " +str(food_details[i]['Discount(%)']))
                                print("Final Price as per Qnt: " +str(food_details[i]['Final Price as per Qnt']))
                                print("Total Stock: "+str((food_details[i]["Total Stock"])))
                                print("Available Stock: "+str((food_details[i]["Available Stock"])))
                                print("Food Order By User: " ,len(food_details[i]['Food Order By User']))
                                print("Total Income: " +str(food_details[i]['Total Income']))
                                print("Received Income: " +str(food_details[i]['Received Income']))
                                print("Percentage of Received Income: "+str(food_details[i]["Percentage of Received Income"]))
                                print('\n')
#----------------------------------------------------------------------------------------------------------------------------------Done
                    elif choice3==3:
                        print("Enter Food ID")
                        Food_ID=input()
                        with open('food.json','r') as file3:
                            try:
                                content3=str(json.load(file3))
                                if Food_ID not in content3:
                                    print("Invalid Food ID")
                                    continue
                            except JSONDecodeError:
                                print("Food not available")
                                continue
                        food_details_by_id=food_operations.View_Food_Details_ByID(admin_name,'food.json',Food_ID)
                        print("Food Name: " +str(food_details_by_id[0]['Food Name']))
                        print("Food Quantity: " +str(food_details_by_id[0]['Food Quantity']))
                        print("Food Initial Price: " +str(food_details_by_id[0]['Food Initial Price']))
                        print("Discount(%): " +str(food_details_by_id[0]['Discount(%)']))
                        print("Final Price as per Qnt: " +str(food_details_by_id[0]['Final Price as per Qnt']))
                        print("Total Stock: "+str(food_details_by_id[0]["Total Stock"]))
                        print("Available Stock: "+str(food_details_by_id[0]["Available Stock"]))
                        print("Food Order By User: " ,len(food_details_by_id[0]['Food Order By User']))
                        print("Total Income: " +str(food_details_by_id[0]['Total Income']))
                        print("Received Income: " +str(food_details_by_id[0]['Received Income']))
                        print("Percentage of Received Income: "+str(food_details_by_id[0]["Percentage of Received Income"]))
                        print('\n')
#----------------------------------------------------------------------------------------------------------------------------------Done
                    elif choice3==4:#update food
                        print("Enter Food ID:")
                        Food_ID=input()
                        #----------------------------------------------------------------------------------Entered ID : Food Details
                        with open('food.json','r') as file3:
                            try:
                                content3=str(json.load(file3))
                                if Food_ID not in content3:
                                    print("Invalid Food ID")
                                    continue
                            except JSONDecodeError:
                                print("Food not available")
                                continue
                        food_details_by_id=food_operations.View_Food_Details_ByID(admin_name,'food.json',Food_ID)
                        print("Food Name: " +str(food_details_by_id[0]['Food Name']))
                        print("Food Quantity: " +str(food_details_by_id[0]['Food Quantity']))
                        print("Food Initial Price: " +str(food_details_by_id[0]['Food Initial Price']))
                        print("Discount(%): " +str(food_details_by_id[0]['Discount(%)']))
                        print("Final Price as per Qnt: " +str(food_details_by_id[0]['Final Price as per Qnt']))
                        print("Total Stock: "+str(food_details_by_id[0]["Total Stock"]))
                        print("Available Stock: "+str(food_details_by_id[0]["Available Stock"]))
                        print("Food Order By User: " ,len(food_details_by_id[0]['Food Order By User']))
                        print("Total Income: " +str(food_details_by_id[0]['Total Income']))
                        print("Received Income: " +str(food_details_by_id[0]['Received Income']))
                        print("Percentage of Received Income: "+str(food_details_by_id[0]["Percentage of Received Income"]))
                        print('\n')
                        #----------------------------------------------------------------------------------
                        print("Enter details to be Updated")
                        print("Enter New Food Name:")
                        new_food_name=input()
                        try:
                            print("Enter New Food Quantity : ")
                            new_food_qnt=int(input())
                            print("Enter New Total Stock : ")
                            new_total_stock=int(input())
                            print("Enter Food Price(RS) : ")
                            new_food_initial_price=float(input())
                            print("Discount(%) : ")
                            new_discount=float(input())
                            new_final_price_as_per_qnt=new_food_initial_price-(new_food_initial_price*(new_discount/100))
                            print("Final price of Food as per Qnt(RS) : ",new_final_price_as_per_qnt)
                            new_total_income=(new_total_stock/new_food_qnt)*new_final_price_as_per_qnt
                            new_food_order_by_user=food_details_by_id[0]['Food Order By User']
                            total=0
                            for i in range(len(food_details[0]['Food Order By User'])):
                                total=total+food_order_by_user[i]["Total Bill"]
                            received_income=total
                            new_percentage_of_received_income=(received_income/new_total_income)*100
                        except ValueError:
                            print("Please enter valid data")
                            continue
                        if (len(new_food_name)*len(Food_ID)*len(str(new_food_qnt))*len(str(new_total_stock))*len(str(new_food_initial_price))*len(str(new_discount))==0) and new_discount>100:
                            print("Please enter valid data")
                            continue
                        else:
                            update_details=food_operations.Update_Food(admin_name,'food.json',Food_ID,new_food_name,new_food_qnt,new_food_initial_price,new_discount,new_final_price_as_per_qnt,new_total_stock,new_total_stock,new_food_order_by_user,new_total_income,received_income,new_percentage_of_received_income)
                        
                        if update_details==False:
                            print("Cannot update food")
                        else:
                            print("Food updated successfully")
#----------------------------------------------------------------------------------------------------------------------------------Done
                    elif choice3==5:#delete food
                        print("Enter Food ID")
                        Food_ID=input()
                        with open('food.json','r+') as file5:
                            try:
                                content5=str(json.load(file5))
                            except JSONDecodeError:
                                print("No Food is added")
                                continue
                        if Food_ID not in content5:
                            print("Invalid Food ID")
                            continue
                        if len(Food_ID)==0:
                            print("Please enter valid data")
                            continue
                        else:
                            delete_details=food_operations.Delete_Food(admin_name,'food.json',Food_ID)
                        if delete_details==True:
                            print("Food deleted successfully")
                        else:
                            print("Cannot delete Food")
#----------------------------------------------------------------------------------------------------------------------------------
                    elif choice3==0:
                        break
                    else:
                        print("Ivalid Option")
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------Done
        elif choice2==2:
            print("Enter Email:")
            Email=input()
            print("Enter Password:")
            Password=input()
            user_login_details=food_operations.Login('user','admin.json','user.json',Email,Password)
            if user_login_details==False:
                print("Invalid Credentials")
                continue
            else:
                with open('user.json','r') as file6:
                    content6=json.load(file6)
                    user_name=""
                    for i in range(len(content6)):
                        if content6[i]["Email"]==Email and content6[i]["Password"]==Password:
                            user_name=content6[i]["Full Name"]
                            break
                print("Welcome "+str(user_name))
                while True:
                    print("Press:")
                    print("1: Order Foods")
                    print("2: View Ordered Foods")
                    print("3: View Food Details by ID")
                    print("4: Update Password")
                    print("0: Logout")
                    try:
                        choice4=int(input())
                    except ValueError:
                        print("Please enter valid choice")
#----------------------------------------------------------------------------------------------------------------------------------Pending
                    if choice4==1:
                        view_food_details=food_operations.View_all_Foods('food.json')
                        if len(view_food_details)==0:
                            print("No Foods available")
                        else:
                            print("All Foods: ")
                            for i in range(len(view_food_details)):
                                # view=view_details[i]
                                print("Food ID: "+str(view_food_details[i]['Food Id']))
                                print("Food Name: " +str(view_food_details[i]['Food Name']))
                                print("Admin Name: " +str(view_food_details[i]['Admin Name']))
                                print("Food Quantity: " +str(view_food_details[i]['Food Quantity']))
                                print("Food Initial Price: " +str(view_food_details[i]['Food Initial Price']))
                                print("Discount: " +str(view_food_details[i]['Discount(%)']))
                                print("Final Price as per Qnt: " +str(view_food_details[i]['Final Price as per Qnt']))
                                print('\n')
                        print("Enter Food ID: ")
                        Food_ID=input()
                        
                        try:
                            for i in range(len(view_food_details)):
                                if view_food_details[i]["Food Id"]==Food_ID:
                                    print("Enter Mobile Number :")
                                    Mobile_No=input()
                                    print("Enter Address :")
                                    Address=input()
                                    print("Enter Food Quantity :")
                                    Food_Quantity=int(input())
                                    if Food_Quantity>view_food_details[i]["Available Stock"]:
                                        print("Food not Available")
                                    elif Food_Quantity<view_food_details[i]["Food Quantity"]:
                                        print("Entered Food Quantity is less !! Please enter Quantity as per food Quantity")
                                    else:
                                        amount=(view_food_details[i]["Final Price as per Qnt"]) / (view_food_details[i]["Food Quantity"])
                                        Total_Bill=amount*Food_Quantity
                                        print("Your Total Bill as per given quantity is : ",Total_Bill)
                                        total=0
                                        for j in range(len(view_food_details[i]["Food Order By User"])):
                                            total=total+view_food_details[i]["Food Order By User"][j]["Total Bill"]
                                        received_income=total
                                        percentage_of_received_income=(received_income/view_food_details[i]["Total Income"])*100
                                else:
                                    print("Invalid Food ID")
                        except ValueError:
                            print("Please enter correct details")

                        food_order_details=food_operations.Order_Food(user_name,'food.json',Food_ID,Mobile_No,Address,Food_Quantity,Total_Bill,received_income,percentage_of_received_income)
                        choice5=input("Please confirm \n1.Yes\n2.No\n")
                        if choice5=="1" and food_order_details==True:

                            print("Food successfully ordered")
                        elif choice5=="1" and food_order_details==False:
                            print("Food not available")
                        elif content5=="2":
                            print("Thank You")
                            break
                        else:
                            print("Please enter valid choice")
                            continue

#----------------------------------------------------------------------------------------------------------------------------------Pending
                    elif choice4==2:
                        all_ordered_foods=[]
                        fetch_details=food_operations.fetch_all_foods('user.json',user_name,all_ordered_foods)
                        if fetch_details:
                            print("All Ordered Foods: ")
                            for i in range(len(all_ordered_foods)):
                                print("Food ID: "+str(all_ordered_foods[i]['Food Id']))
                                print("Food Name: " +str(all_ordered_foods[i]['Food Name']))
                                print("Admin Name: " +str(all_ordered_foods[i]['Admin Name']))
                                print("Food Quantity: " +str(all_ordered_foods[i]['Food Quantity']))
                                print("Food Initial Price: " +str(all_ordered_foods[i]['Food Initial Price']))
                                print("Discount: " +str(all_ordered_foods[i]['Discount']))
                                print("Final Price as per Qnt: " +str(all_ordered_foods[i]['Final Price as per Qnt']))
                                print('\n')
                        else:
                            print("No food has been ordered")
#----------------------------------------------------------------------------------------------------------------------------------Pending
                    elif choice4==3:
                        print("Enter food ID")
                        Food_ID=input()
                        with open('food.json','r') as file8:
                            try:
                                content8=str(json.load(file8))
                                if Food_ID not in content8:
                                    print("Invalid Food ID")
                                    continue
                            except JSONDecodeError:
                                print("Foods not available")
                                continue
                        view_events_by_id=food_operations.View_Food_ByID('food.json',Food_ID)
                        print("Event Name: " +str(view_events_by_id[0]['Name']))
                        print("Start Date: " +str(view_events_by_id[0]['Start Date']))
                        print("Start Time: " +str(view_events_by_id[0]['Start Time']))
                        print("End Date: " +str(view_events_by_id[0]['End Date']))
                        print("End Time: " +str(view_events_by_id[0]['End Time']))
                        print("End Time: " +str(view_events_by_id[0]['End Time']))
                        print("Organizer: "+str(view_events_by_id[0]["Organizer"]))
                        print("Seats Available: "+str(view_events_by_id[0]['Seats Available']))
                        print('\n')
#----------------------------------------------------------------------------------------------------------------------------------Pending
                    elif choice4==4:
                        print("Enter new password")
                        password=input()
                        if(len(password))<4:
                            print("Please enter valid data")
                            continue
                        update_password=food_operations.Update_Password('user.json',user_name,password)
                        if update_password==True:
                            print("Password updated successfully")
                        else:
                            print("Cannot update password")
#----------------------------------------------------------------------------------------------------------------------------------
                    elif choice4==0:
                        break
                    else:
                        print("Invalid Choice, Please enter again")
                        continue
#----------------------------------------------------------------------------------------------------------------------------------
    elif choice==0:
        break
    else:
        print("Invalid Choice, Please enter again")
        continue