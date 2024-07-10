import operation
import json
if __name__=="__main__":
    while True:
        try:
            choice=int(input("Press \n1.Register \n2.Login \n3.Exit \n"))
        except ValueError:
            print("Please enter correct choice")
            continue

        if choice==1:
            name=input("Enter Your Name : ")
            user_name=input("Enter your User Name : ")
            password=input("Enter your Password : ")
            operation.Register("user.json",name,user_name,password)
            print("Registered successfully")

        elif choice==2:
            user_name=input("Enter User name :")
            password=input("Enter Password :")
            op=operation.Login('user.json',user_name,password)
            if op==False:
                print("Invalid Credentials")
                continue
            else:
                file=open('user.json','r')
                content=json.load(file)
                file.close()
                name=""
                for i in range(len(content)):
                    if content[i]["User Name"]==user_name and content[i]["Password"]==password:
                        name=content[i]["Name"]
                        break
                print("Welcome "+str(name))

        elif choice==3:
            print("  Thank you  ")
            break
    
