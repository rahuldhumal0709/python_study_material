'''1-1000,1100,1200,...,2100,
2-2200,2300,2400,...,3300,
3-3400,3500,3600,...,4500,
.
.
.
10-11800,11900,12000,...,12900
'''
year = {1:'2025',2:'2026',3:'2027',4:'2028',5:'2029',6:'2030',7:'2031',8:'2032',9:'2033',10:'2034'}
month = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
total_investimate = 0
amount = 1000
interest = 7.0
total_amount = 0
for i in range(1,11):#2025-2034
    this_year_total = 0
    for j in range(1,13):#jan-dec
        print(f'{year[i]} : {month[j]} = {amount}')
        if j==6 or j==7:#count total amount of the current year using middle year
            this_year_total += amount
        total_investimate += amount
        amount = amount + 100
    this_year_total *= 6
    # print('Total investimate of this year : ',this_year_total)
    total_amount += total_investimate + (0.01 * total_investimate) * interest
    print()
print('Total investimate of 10 year : ',total_investimate)
print('Total amount after 10 year : ',total_amount)
print()
