-- Companies Table
CREATE TABLE Companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

-- Skills Table
CREATE TABLE Skills (
    skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

-- Jobs Table
CREATE TABLE Jobs (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    position TEXT,
    title TEXT,
    company_id INTEGER,
    location TEXT,
    post_date DATE,
    work_type TEXT,
    level TEXT,
    seniority_level TEXT,
    remote_friendly TEXT,
    link TEXT,
    FOREIGN KEY (company_id) REFERENCES Companies(company_id)
);

-- JobSkills Join Table (Many-to-Many)
CREATE TABLE JobSkills (
    job_id INTEGER,
    skill_id INTEGER,
    PRIMARY KEY (job_id, skill_id),
    FOREIGN KEY (job_id) REFERENCES Jobs(job_id),
    FOREIGN KEY (skill_id) REFERENCES Skills(skill_id)
);