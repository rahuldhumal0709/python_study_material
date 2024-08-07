import json
import string
import random
from json import JSONDecodeError
from datetime import datetime

def Register(type,gamers_json_file,sellers_json_file,Email_ID,Username,Password,Contact_Number):
    '''Register Function || Already Given'''
    if type.lower()=='seller':
        f=open(sellers_json_file,'r+')
        d={
            "Email":Email_ID,
            "Username":Username,
            "Password":Password,
            "Contact Number":Contact_Number,
        }
        try:
            content=json.load(f)
            if d not in content and d["Username"] not in str(content):
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
        return True
    elif type.lower()=='gamer':
        f=open(gamers_json_file,'r+')
        d={
            "Email":Email_ID,
            "Username":Username,
            "Password":Password,
            "Contact Number":Contact_Number,
            "Wishlist":[],
            "Cart":[],
        }
        try:
            content=json.load(f)
            if d not in content and d["Username"] not in str(content):
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()

def Login(type,gamers_json_file,sellers_json_file,Username,Password):
    '''Login Functionality || Return True if successfully logged in else False || Already Given'''
    d=0
    if type.lower()=='seller':
        f=open(sellers_json_file,'r+')
    else:
        f=open(gamers_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        return False
    for i in range(len(content)):
        if content[i]["Username"]==Username and content[i]["Password"]==Password:
            d=1
            break
    f.seek(0)
    f.truncate()
    json.dump(content,f)
    f.close()
    if d==0:
        return False
    return True

def AutoGenerate_ProductID():
    '''Return a autogenerated random product ID || Already Given'''
    product_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=4))
    return product_ID

def AutoGenerate_OrderID():
    '''Return a autogenerated random product ID || Already Given'''
    Order_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Order_ID

def days_between(d1, d2):
    '''Calculating the number of days between two dates || Already Given'''
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def Create_Product(owner,product_json_file,product_ID,product_title,product_type,price_per_day,total_stock_available):
    '''Creating a product || Return True if successfully created else False'''
    '''---------Write your code below---------'''
    d={
        "Seller Username":owner,
        "Product ID":product_ID,
        "Product Title":product_title,
        "Product Type":product_type,
        "Price Per Day":price_per_day,
        "Total Stock Available":total_stock_available
    }
    f=open(product_json_file,'r+')
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
    f.close()


def Fetch_all_Products_created_by_seller(owner,product_json_file):
    '''Get all products created by the seller(owner)'''
    '''---------Write your code below---------'''
    details=[]
    f=open(product_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        if content[i]["Seller Username"]==owner:
            details.append(content[i])
    return details
    

def Fetch_all_products(products_json_file):
    '''Get all products created till now || Helper Function'''
    '''Already Given'''
    All_Products_list=[]
    f=open(products_json_file,'r')
    try:
        content=json.load(f)
        All_Products_list=content
    except JSONDecodeError:
        pass
    return All_Products_list

def Fetch_Product_By_ID(product_json_file,product_ID):
    '''Get product deatils by product ID'''
    Details=[]
    f=open(product_json_file,'r+')
    content1=json.load(f)
    for i in range(len(content1)):
        if content1[i]["Product ID"]==product_ID:
            Details.append(content1[i])
            break
    f.close()
    return Details

def Update_Product(Username,product_json_file,product_ID,detail_to_be_updated,new_value):
    '''Updating Product || Return True if successfully updated else False'''
    d=0
    f=open(product_json_file,'r+')
    content2=json.load(f)
    for i in range(len(content2)):
        if content2[i]["Product ID"]==product_ID and detail_to_be_updated in content2[i].keys() and content2[i]["Seller Username"]==Username and detail_to_be_updated!="Product ID":
            content2[i][detail_to_be_updated]=new_value
            d=1
            break
    f.seek(0)
    f.truncate()
    json.dump(content2,f)
    f.close()
    if d==1:
        return True
    return False

def Add_item_to_wishlist(Username,product_ID,gamers_json_file):
    '''Add Items to wishlist || Return True if added successfully else False'''
    '''---------Write your code below---------'''
    f=open(gamers_json_file,'r+')
    d=0
    content2=json.load(f)
    for i in range(len(content2)):
        if content2[i]["Username"]==Username:
            content2[i]["Wishlist"].append(product_ID)
            d=1
            break

    f.seek(0)
    f.truncate()
    json.dump(content2,f)
    f.close()
    if d==1:
        return True
    return False
    

def Remove_item_from_wishlist(Username,product_ID,gamers_json_file):
    '''Remove items from wishlist || Return True if removed successfully else False'''
    '''---------Write your code below---------'''
    f=open(gamers_json_file,'r+')
    d=0
    content2=json.load(f)
    for i in range(len(content2)):
        if content2[i]["Username"]==Username:
            content2[i]["Wishlist"].remove(product_ID)
            d=1
            break

    f.seek(0)
    f.truncate()
    json.dump(content2,f)
    f.close()
    if d==1:
        return True
    return False

def Add_item_to_cart(Username,product_ID,Quantity,gamers_json_file,booking_start_date,booking_end_date,products_json_file):
    '''Add item to the cart || Check whether the quantity mentioned is available || Return True if added successfully else False'''
    '''Add the Product ID, Quantity, Price, Booking Start Date, Booking End Date in the cart as list of dictionaries'''
    '''---------Write your code below---------'''
    f=open(gamers_json_file,'r+')
    f1=open(products_json_file,'r')
    d={
        "Product ID":product_ID,
        "Quantity":Quantity,
        "Booking Start Date":booking_start_date,
        "Booking End Date":booking_end_date
        }
    content=json.load(f)
    content1=json.load(f1)
    for j in range(len(content1)):
        if d["Product ID"] in content1[j]:
            for i in range(len(content)):
                if content[i]["Username"]==Username:
                    lst=content[i]["Cart"]
                    if d not in lst:
                        lst.append(d)
                        f.seek(0)
                        f.truncate()
                        json.dump(content,f)
                        f.close()
                        f1.close()
                        return True
    f.close()
    f1.close()
    return False
    

def Remove_item_from_cart(Username,product_ID,gamers_json_file):
    '''Remove items from the cart || Return True if removed successfully else False'''
    '''---------Write your code below---------'''
    f=open(gamers_json_file,'r+')
    d=0
    content2=json.load(f)
    for i in range(len(content2)):
        if content2[i]["Username"]==Username:
            for j in range(len(content2[i]["Cart"])):
                if content2[i]["Cart"][j]["Product ID"]==product_ID:
                    del content2[i]["Cart"][j]
                    d=1
                    break

    f.seek(0)
    f.truncate()
    json.dump(content2,f)
    f.close()
    if d==1:
        return True
    return False

def View_Cart(Username,gamers_json_file):
    '''Return the current cart of the user'''
    f=open(gamers_json_file,'r')
    cart=[]
    try:
        content=json.load(f)
        for i in range(len(content)):
            if content[i]["Username"]==Username:
                cart=content[i]["Cart"]
                break
        return cart
    except JSONDecodeError:
        return cart

def Place_order(Username,gamers_json_file,Order_Id,orders_json_file,products_json_file):
    '''Place order || Return True is order placed successfully else False || Decrease the quantity of the product orderd if successfull'''
    '''---------Write your code below---------'''

    

def View_User_Details(gamers_json_file,Username):
    '''Return a list with all gamer details based on the username || return an empty list if username not found'''
    '''---------Write your code below---------'''
    details=[]
    f=open(gamers_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        if content[i]["Username"]==Username:
            details.append(content[i])
    return details
    

def Update_User(gamers_json_file,Username,detail_to_be_updated,updated_detail):
    '''Update the detail_to_be_updated of the user to updated_detail || Return True if successful else False'''
    '''---------Write your code below---------'''
    f=open(gamers_json_file,"r+")
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["Username"]==Username:
            try:
                a=content[i][detail_to_be_updated]
            except KeyError:
                return False
            content[i][detail_to_be_updated]=updated_detail
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close()
            return True
    f.close()
    return False
    

def Fetch_all_orders(orders_json_file,Username):
    '''Fetch all previous orders for the user and return them as a list'''
    orders=[]
    f=open(orders_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return orders
    for i in range(len(content)):
        if content[i]["Ordered by"]==Username:
            orders.append(content[i])
    return orders
    

