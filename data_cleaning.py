import pandas as pd

df = pd.read_csv("fifa players.csv")

print("Before:", df.shape)

df = df.drop_duplicates()

df["national_team"] = df["national_team"].fillna("Not Selected")
df["national_team_position"] = df["national_team_position"].fillna("Not Selected")
df["national_rating"] = df["national_rating"].fillna(0)
df["national_jersey_number"] = df["national_jersey_number"].fillna(0)

df["value_euro"] = df["value_euro"].fillna(df["value_euro"].median())
df["wage_euro"] = df["wage_euro"].fillna(df["wage_euro"].median())
df["release_clause_euro"] = df["release_clause_euro"].fillna(df["release_clause_euro"].median())

df["main_position"] = df["positions"].str.split(",").str[0]

df.to_csv("cleaned_fifa_players.csv", index=False)

print("After:", df.shape)
print("Cleaning completed")