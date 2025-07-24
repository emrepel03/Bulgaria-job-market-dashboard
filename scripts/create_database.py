import sqlite3

# === Connect to SQLite DB ===
conn = sqlite3.connect("data/jobs_data.db")
cursor = conn.cursor()

# === Create Tables ===
cursor.execute("""
CREATE TABLE IF NOT EXISTS Companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Jobs (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    position TEXT,
    post_date TEXT,
    work_type TEXT,
    level TEXT,
    company_id INTEGER,
    location TEXT,
    link TEXT,
    FOREIGN KEY (company_id) REFERENCES Companies(company_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Skills (
    skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS JobSkills (
    job_id INTEGER,
    skill_id INTEGER,
    FOREIGN KEY (job_id) REFERENCES Jobs(job_id),
    FOREIGN KEY (skill_id) REFERENCES Skills(skill_id),
    PRIMARY KEY (job_id, skill_id)
);
""")

conn.commit()
conn.close()

print("✅ Database and tables created successfully.")