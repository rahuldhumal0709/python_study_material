import datetime as dt
def calculate_subscription(expiry_date,months_to_buy,monthly_cost):
    
    if expiry_date.day >= 1 and expiry_date.day <= 14:

        Mnth=(expiry_date.month-1 + months_to_buy) % 12 + 1 # calculate month
        Yr=expiry_date.year + (expiry_date.month-1 + months_to_buy) // 12 # calculate year
        Day=1
        new_expiry=dt.date(Yr,Mnth,Day)
        resDays=new_expiry-expiry_date
        cost=(monthly_cost / 30)*resDays.days
        return new_expiry ,cost

    elif expiry_date.day >= 15 and expiry_date.day <= 31:
        
        Mnth=(expiry_date.month-1 + months_to_buy) % 12 + 1
        Yr=expiry_date.year + (expiry_date.month-1 + months_to_buy) // 12
        Day=15
        new_expiry=dt.date(Yr,Mnth,Day)
        resDays=new_expiry-expiry_date
        cost=(monthly_cost / 30)*resDays.days
        return new_expiry ,cost
    
res=calculate_subscription(dt.date(2022,6,16),1,1000)
print(res)