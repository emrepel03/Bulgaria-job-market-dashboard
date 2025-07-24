import pandas as pd
import re
import numpy as np

# === Load Data ===
df = pd.read_csv("data/raw/tech_jobs_raw.csv")

# === Deduplication ===
df.drop_duplicates(subset=["Title", "Company", "Date"], inplace=True)

# === Specific cleaning ===

# Fix encoding issues in Position column
df["Position"] = df["Position"].str.replace("%20", " ")

# Normalize Location names
df["Location"] = df["Location"].astype(str)
df["Location"] = df["Location"].apply(lambda x: 
    "Sofia" if "sofia" in x.lower() else
    "Varna" if "varna" in x.lower() else
    "Plovdiv" if "plovdiv" in x.lower() else x)

# Remove irrelevant locations
df = df[~df["Location"].str.lower().str.contains("pernik")]
df = df[~df["Location"].str.lower().str.contains("ukraine")]

# === Standardize Formats ===
df["Location"] = df["Location"].astype(str).str.strip().str.title()
df["Company"] = df["Company"].astype(str).str.strip().str.title()
df["Title"] = df["Title"].astype(str).str.strip()

if "WorkType" in df.columns:
    df["WorkType"] = df["WorkType"].where(df["WorkType"].notna(), None) 
    df["WorkType"] = df["WorkType"].apply(lambda x: x.strip() if isinstance(x, str) else x)

df["Level"] = df["Level"].astype(str).str.strip().str.title()
df["Skills"] = df["Skills"].fillna("Not specified").astype(str).str.strip()
df["Skills"] = df["Skills"].str.replace(", less", "", regex=False)

# === Feature: Detect Remote-Friendly from Title or Skills ===
def detect_remote(row):
    text = f"{row['Title']} {row['Skills']}".lower()
    if "remote" in text: return "Remote"
    if "hybrid" in text: return "Hybrid"
    return "On-site"

df["WorkType"] = df.apply(detect_remote, axis=1) 

#drop column WorkType

df.drop(columns="WorkType", inplace=True)

# === Export Cleaned Data ===
df.to_csv("data/cleaned/tech_jobs_cleaned.csv", index=False)

# === Optional: Print Summary ===
print("✅ Cleaning complete.")
print(f"Rows after deduplication: {len(df)}")
print(f"File saved: data/cleaned/tech_jobs_cleaned.csv")