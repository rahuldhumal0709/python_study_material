# CSV - Comma Seperated Value
# extension - .csv
# all the data in this file are seperated by comma

import csv

with open("D:\\DS\\Edyoda(DS290822B)\\Python\\DS290822B\\_1_Python\\_20_csv\\test.csv","r") as file:
    data = csv.reader(file)
    
    # header = next(data)
    # print(header)

    # print()
    lst = []
    for i in data:
        lst.append(i)

    # print(lst)

    # count = data.line_num
    # print("Count : ",count)

    # print()
    for i in lst[1:]:
        print(i)