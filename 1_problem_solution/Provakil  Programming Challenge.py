#!/usr/bin/env python
# coding: utf-8

# In[15]:


import datetime as dt
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_subscription(expiry_date,months_to_buy,monthly_cost):
    try:
        d=datetime.strptime(expiry_date,'%d/%m/%Y').date()  
    except ValueError as e:
        print('Invalid Date')
        return      
    new_d=d+relativedelta(months=+months_to_buy)
    day=new_d.day
    daily_cost=monthly_cost/30
    if day==1 or day==15:
        new_expiry=new_d
        cost=float(months_to_buy*monthly_cost)
    else:    
        if day>15:
            new_expiry=new_d+relativedelta(day=15)           
        elif day>1:
            new_expiry=new_d+relativedelta(day=1)           
        diff=relativedelta(new_expiry,d)
        cost=round(diff.days*daily_cost +diff.months*monthly_cost,2)    
    return new_expiry.strftime('%d/%m/%Y'),cost
print(calculate_subscription("19/06/2022", 1, 1000)) 

