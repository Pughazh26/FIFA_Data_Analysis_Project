import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_fifa_players.csv")

# Take Top 100 players based on Overall Rating
top100 = df.sort_values(by="overall_rating", ascending=False).head(100)

# Save into new CSV
top100.to_csv("fifa_100_players.csv", index=False)

print("Top 100 players dataset created successfully!")
print(top100.shape)