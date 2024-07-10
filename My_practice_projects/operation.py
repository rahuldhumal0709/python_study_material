import json
from json import JSONDecodeError
def Register(user_json_file,name,user_name,password):
    f=open(user_json_file,'r+')
    d={
        "Name":name,
        "User Name":user_name,
        "Password":password
    }
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
def Login(user_json_file,user_name,password):
    d=0
    f=open(user_json_file,'r')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["User Name"]==user_name and content[i]["Password"]==password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True