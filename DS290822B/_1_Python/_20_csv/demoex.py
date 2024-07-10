import pandas as pd
d=[{"Name":"KL","No":"1","Team":"India"},{"Name":"Virat","No":"18","Team":"India"},{"Name":"Dhoni","No":"7","Team":"India"}]
df=pd.DataFrame(d)
# print(df)
# df.to_csv("cricket.csv")

my_csv=pd.read_csv("cricket.csv",index_col=0)
print(my_csv)