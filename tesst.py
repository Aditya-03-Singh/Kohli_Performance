import pandas as pd 

data = {
    "apples": [4,3,6,1],
    "oranges":[3,7,4,1]
}
index_titles =[
    "Arun","Shaun","JAmes", "Wilson"
]
df = pd.DataFrame(data,index=index_titles)

print(df.loc["Arun"])

print(df["oranges"].iloc[0:1])
