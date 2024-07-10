s1={"name= ":"Rahul",
            "Roll_no":"CS3145",
            "Eng":70,
            "Math":90,
            "Sci" :80
 }
s2={"name= ":"Dipak",
            "Roll_no":"CS3146",
            "Eng":90,
            "Math":60,
            "Sci" :70
 }
s3={"name= ":"Sanket",
            "Roll_no":"CS3147",
            "Eng":80,
            "Math":70,
            "Sci" :60
 }
s4={"name= ":"Saurabh",
            "Roll_no":"CS3148",
            "Eng":90,
            "Math":70,
            "Sci" :70
 }
s5={"name= ":"Vitthal",
            "Roll_no":"CS3149",
            "Eng":90,
            "Math":70,
            "Sci" :75
 }
l=[s1,s2,s3,s4,s5]
# sum=[]
# avg=[]
for s in l:
    s["Total"]=s["Eng"]+s["Math"]+s["Sci"]
    a=s["Total"]//3
    s["Average"]=a
    print(s)
print()

max=s["Average"]
# print(max)
for i in l:
    if i["Average"]>max:
        max=i["Average"]
        print(max)

min=s["Average"]
for i in l:
    if i["Average"]<min:
        min=i["Average"]
        print(min)
# # print("sum",sum)
# # print("avg",avg)