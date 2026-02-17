import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("Initial dataset shape:", df.shape)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Fill missing values
df.fillna("Unknown", inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)

print("\nMilestone 1 Cleaning Completed Successfully!")
