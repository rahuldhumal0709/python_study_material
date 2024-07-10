import pandas as pd
dict1={
"name":["KL","Virat","Rohit","Dhoni"],
"Age":[30,34,35,41],
"Team":["LSG","RCB","MI","CSK"]
}
df=pd.DataFrame(dict1)
# print(df)

# df.to_csv("players.csv")
# df.to_csv("players_index_falls.csv",index=False)

# print("Head : ",df.head(2))
# print("Tail : ",df.tail(2))
# print(df.describe())

read=pd.read_csv("players1.csv")
# print(read)
# print(read["name"])
# read["name"][0]="KLR"
read.index=["First","Second","Third","Fourth"]
print(read)
# read.to_csv("players1.csv")
