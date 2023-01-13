import pandas as pd 

df = pd.read_csv("Virat_Kohli (1).csv")

print (df.head(10))

# print (df.tail(10))

# df.info()
# print(df.shape)

print(df.describe())

print(df.columns)

print

run_frequency = df["Runs"].value_counts()
print(run_frequency)

new_df = df[["Runs","SR", "Opposition"]]
print(new_df)

# find all the matches where virat scored a century
tons = df[df["Runs"] >=100]
print(tons)

#strike rate > 100
ton_SR = df[df["SR"] >100]
print(ton_SR)

# played with sri lanka and scored a century

# Sri_cent = (df (df["Opposition"]=="v Srilanka")& (df["Runs"]>=100))
# print(Sri_cent)

def find_centuries(x):
    if x >= 100:
        return "OG"
    else:
        return "Noob"
df["Centuries"]= df["Runs"].apply(find_centuries)
print(df.tail(10))



