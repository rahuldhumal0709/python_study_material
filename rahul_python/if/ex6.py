runs=0
name=input("Enter Name of Player : ")
Country=input("Enter Country : ")
Jno=int(input("Enter Jersey Number : "))
Opp=input("Opposition Team : ")
Innings=int(input("Enter total number of innings : "))
for i in range(1,Innings):
    runs=runs+i
Notout=int(input("Enter notout innings : "))
total=Innings-Notout
Avg=runs/total
print(Avg)