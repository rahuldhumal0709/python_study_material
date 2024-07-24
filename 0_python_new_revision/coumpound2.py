year = {1:'2025',2:'2026',3:'2027',4:'2028',5:'2029',6:'2030',7:'2031',8:'2032',9:'2033',10:'2034'}
month = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
total_investimate = 2000000
interest = 9.0
total_amount = 0
for i in range(1,11):#2025-2034
    total_amount = total_investimate + (0.01 * total_investimate) * interest
    total_investimate = total_amount
    print(f'Total amount after {i} year : ',total_amount)
print('Total amount after 10 year : ',total_amount)
print()
