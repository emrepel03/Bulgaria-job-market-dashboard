import pandas as pd

# === Load Cleaned Dataset ===
df = pd.read_csv("data/cleaned/tech_jobs_cleaned.csv")

# === Normalize Placeholder Values ===

print("=== Data Validation Report ===\n")

# === 1. Basic Summary Statistics ===
print("→ Basic Stats")
print("Total Job Postings:", len(df))
print("Unique Companies:", df['Company'].nunique())
print("Unique Titles:", df['Title'].nunique())
print("Date Range:", df['Date'].min(), "to", df['Date'].max())
print("\nMissing Values Per Column:")
print(df.isnull().sum())
print("=" * 50)

# === 2. Postings Per Company ===
print("\n→ Top Companies by Number of Postings:")
print(df['Company'].value_counts().head(10))
print("=" * 50)

# === 3. Postings Per Date ===
print("\n→ Job Postings by Date:")
print(df['Date'].value_counts().sort_index())
print("=" * 50)

# === 4. Check for Duplicate Postings ===
dupes = df.duplicated(subset=["Title", "Company", "Location", "Date"])
print("\n→ Duplicate Job Postings:")
print("Duplicate count:", dupes.sum())
print("=" * 50)

# === 5. Spot-Check Random Rows ===
print("\n→ Spot Check (5 Random Jobs):")
print(df.sample(5, random_state=42))
print("=" * 50)

# === 6. Column Names & Sample Values ===
print("\n→ Column Overview:")
print("Columns:", df.columns.tolist())
# print("WorkType Sample:", df['WorkType'].dropna().unique()[:5])
# print("SeniorityLevel Sample:", df['SeniorityLevel'].dropna().unique()[:5])
# print("RemoteFriendly Sample:", df['RemoteFriendly'].dropna().unique()[:5])
print("=" * 50)

print("\n✅ Validation complete.\n")