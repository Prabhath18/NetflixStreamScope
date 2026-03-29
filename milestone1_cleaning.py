import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("Initial dataset shape:", df.shape)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Create new columns
df["month_added"] = df["date_added"].dt.month
df["year_added"] = df["date_added"].dt.year

# Fill ONLY object columns (NOT datetime)
object_cols = df.select_dtypes(include="object").columns
df[object_cols] = df[object_cols].fillna("Unknown")

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)

print("\nMilestone 1 Cleaning Completed Successfully!")