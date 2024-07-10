# Q18.Python program to calculate stats of a cricket player against an opposition.

def find_players_avg():
    name=input("Enter Name of Player : ")
    Jno=int(input("Enter Jersey Number : "))
    Opp=input("Opposition Team : ")
    innings=int(input("Enter total number of innings : "))
    runs=0
    for i in range(1,innings+1):
        inn = int(input(f"Enter inning {i} runs : "))
        runs = inn + runs
    not_out=int(input("Enter total not out innings : "))
    outs=innings-not_out
    Avg=runs/outs
    print("\nPlayer name :",name)
    print("Jersey Number :",Jno)
    print("Opposition name : ",Opp)
    print(f"{name}'s total runs against {Opp} : {runs}")
    print(f"{name}'s average against {Opp} : {Avg}")
find_players_avg()