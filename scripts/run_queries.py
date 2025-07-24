import sqlite3
import pandas as pd
import os
import numpy as np

# === Connect to SQLite database ===
conn = sqlite3.connect("data/jobs_data.db")

# === Create output folder if not exists ===
os.makedirs("data/analysis", exist_ok=True)

# === Query 1: Jobs per Company ===
df1 = pd.read_sql_query("""
    SELECT C.name AS company, COUNT(*) AS job_count
    FROM Jobs J
    JOIN Companies C ON J.company_id = C.company_id
    GROUP BY C.company_id
    ORDER BY job_count DESC
""", conn)
df1.to_csv("data/analysis/jobs_per_company.csv", index=False)

# === Query 2: Jobs per Skill ===
df2 = pd.read_sql_query("""
    SELECT S.name AS skill, COUNT(*) AS job_count
    FROM JobSkills JS
    JOIN Skills S ON JS.skill_id = S.skill_id
    GROUP BY S.skill_id
    ORDER BY job_count DESC
""", conn)
df2.to_csv("data/analysis/jobs_per_skill.csv", index=False)

# === Query 3: Jobs per Position Keyword ===
keywords = ['developer', 'data scientist', 'data analyst', 'machine learning', 'devops', 'qa']
df_list = []

for keyword in keywords:
    query = f"""
        SELECT '{keyword}' AS position, COUNT(*) AS job_count
        FROM Jobs
        WHERE LOWER(position) LIKE '%{keyword}%'
    """
    df = pd.read_sql_query(query, conn)
    df_list.append(df)

df3 = pd.concat(df_list, ignore_index=True)
df3.to_csv("data/analysis/jobs_per_position_keyword.csv", index=False)

# === Query 4: Jobs per Level (with fallback from title) ===
df4 = pd.read_sql_query("""
    SELECT 
        CASE
            WHEN LOWER(level) LIKE '%intern%' OR LOWER(title) LIKE '%intern%' THEN 'Intern'
            WHEN LOWER(level) LIKE '%junior%' OR LOWER(title) LIKE '%junior%' THEN 'Junior'
            WHEN LOWER(level) LIKE '%mid%' OR LOWER(title) LIKE '%mid%' THEN 'Mid'
            WHEN LOWER(level) LIKE '%senior%' OR LOWER(title) LIKE '%senior%' THEN 'Senior'
            WHEN LOWER(level) LIKE '%lead%' OR LOWER(title) LIKE '%lead%' THEN 'Lead'
            WHEN LOWER(level) LIKE '%manager%' OR LOWER(title) LIKE '%manager%' THEN 'Manager'
            ELSE 'Unspecified'
        END AS level_group,
        COUNT(*) AS job_count
    FROM Jobs
    GROUP BY level_group
    ORDER BY job_count DESC
""", conn)
df4.to_csv("data/analysis/jobs_per_level.csv", index=False)

# === Query 6: Jobs per Location ===
df5 = pd.read_sql_query("""
    SELECT location, COUNT(*) AS job_count
    FROM Jobs
    GROUP BY location
    ORDER BY job_count DESC
""", conn)
df5.to_csv("data/analysis/jobs_per_location.csv", index=False)

# === Query 6: Top Roles × Levels Matrix ===

roles = ['developer', 'data analyst', 'data scientist', 'qa', 'devops', 'machine learning']
levels = ['intern', 'junior', 'mid', 'senior', 'lead', 'manager']

matrix = []

for role in roles:
    for level in levels:
        query = f"""
            SELECT COUNT(*) AS count
            FROM Jobs
            WHERE (LOWER(title) LIKE '%{role}%' OR LOWER(position) LIKE '%{role}%')
              AND (LOWER(title) LIKE '%{level}%' OR LOWER(level) LIKE '%{level}%')
        """
        count = pd.read_sql_query(query, conn).iloc[0]['count']
        matrix.append({'role': role.title(), 'level': level.title(), 'count': count})

df6 = pd.DataFrame(matrix)
pivot_df6 = df6.pivot(index='role', columns='level', values='count').fillna(0).astype(int)
pivot_df6.to_csv("data/analysis/top_roles_vs_levels.csv")