import pandas as pd
import sqlite3

# === Load Cleaned CSV ===
df = pd.read_csv("data/cleaned/tech_jobs_cleaned.csv").fillna("")

# === Connect to DB ===
conn = sqlite3.connect("data/jobs_data.db")
cursor = conn.cursor()

# === Clear Existing Data ===
cursor.execute("DELETE FROM JobSkills")
cursor.execute("DELETE FROM Skills")
cursor.execute("DELETE FROM Jobs")
cursor.execute("DELETE FROM Companies")
conn.commit()

# === Insert Companies and Get IDs ===
company_map = {}
for company in df['Company'].unique():
    cursor.execute("INSERT OR IGNORE INTO Companies (name) VALUES (?)", (company,))
    conn.commit()
    cursor.execute("SELECT company_id FROM Companies WHERE name = ?", (company,))
    company_map[company] = cursor.fetchone()[0]

# === Insert Jobs ===
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Jobs (title, position, post_date, level, company_id, location, link)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        row['Title'], row['Position'], row['Date'], row['Level'],
        company_map[row['Company']], row['Location'], row['Link'],
    ))
    conn.commit()

# === Get job_ids after insert ===
job_ids = pd.read_sql("SELECT job_id, link FROM Jobs", conn).set_index("link")["job_id"].to_dict()

# === Insert Skills ===
skill_set = set()
for skills in df['Skills']:
    for skill in [s.strip() for s in skills.split(",") if s.strip()]:
        skill_set.add(skill)

skill_map = {}
for skill in skill_set:
    cursor.execute("INSERT OR IGNORE INTO Skills (name) VALUES (?)", (skill,))
    conn.commit()
    cursor.execute("SELECT skill_id FROM Skills WHERE name = ?", (skill,))
    skill_map[skill] = cursor.fetchone()[0]

# === Link Skills to Jobs ===
for _, row in df.iterrows():
    job_id = job_ids.get(row['Link'])
    if not job_id:
        continue
    for skill in [s.strip() for s in row['Skills'].split(",") if s.strip()]:
        skill_id = skill_map.get(skill)
        if skill_id:
            cursor.execute("INSERT OR IGNORE INTO JobSkills (job_id, skill_id) VALUES (?, ?)", (job_id, skill_id))
            conn.commit()

conn.close()
print("✅ Data loaded into SQLite database.")