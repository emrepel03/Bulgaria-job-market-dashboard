
# Bulgaria Tech Job Market Intelligence Dashboard

**Author**: Emre Pelzer  
**Tools Used**: Python, SQL, Power BI, NLP (Flair), Selenium, Gradio  
**Target Audience**: Recruiters, hiring managers, tech professionals, and analysts interested in Bulgaria’s evolving tech job market.

---

## Project Overview

This project analyzes and visualizes over 400 job postings from the top three Bulgarian tech hubs — Sofia, Varna, and Plovdiv — to uncover trends, skill demands, and hiring patterns. It was created to showcase advanced data skills through a full pipeline: from custom AI-powered web scraping to interactive dashboard delivery.

The final result is a Power BI dashboard that gives decision-makers immediate, actionable insights into Bulgaria’s tech job landscape.

---

## Key Features & Highlights

- **Custom Job Scraper**  
  Built with **Selenium** and **BeautifulSoup**, enhanced by **Flair NLP** for automatic skill extraction. Includes a **Gradio UI** allowing users to filter jobs by city, experience level, work type, and more.

- **Full ETL Pipeline**  
  Includes Python scripts for cleaning, validating, and loading data into a structured **SQLite database** with well-defined schema.

- **Powerful Dashboard (Power BI)**  
  Features bar charts, stacked visuals, pie charts, and slicers. Visuals include:
  - Top skills demand (e.g., Python, SQL, Excel)
  - Role-seniority breakdown
  - Company hiring leaderboard
  - And more

- **Organized Repo Structure**
  - `data/`: raw, cleaned, and analyzed datasets
  - `scripts/`: scraping, cleaning, validation, loading
  - `notebooks/`: analysis and visualization planning
  - `dashboard/`: final `.pbix` and `.pdf` file
  - `plots/`: exported visualizations

---

## Key Insights

- **Python** is the most in-demand skill, appearing in over 1 out of 5 postings.
- Most roles are mid-level or senior — junior roles are relatively rare.
- Sofia dominates tech hiring, with Varna and Plovdiv far behind.
- Top companies hiring include **myPOS**, **MentorMate**, and **Luxoft**.
- Skill combinations show strong co-occurrence of Python with SQL and Excel.

---

## Dashboard Preview

See full dashboard layout (PDF): [Bulgaria Tech Market Dashboard (PDF)](dashboard/BulgariaTechMarketDashboard.jpg)

---

## How to Use

1. Clone the repo  
   `git clone https://github.com/emrepel03/bulgaria-job-market-dashboard.git`

2. Open the `.pbix` file in Power BI Desktop (Windows required).  
   File path: `dashboard/BulgariaTechMarketDashboard.pbix`

3. Or explore the data manually:  
   - Check `data/analysis/` for ready-made CSVs
   - View visualizations in `plots/` or `notebooks/exploratory_analysis`
   - Review code in `scripts/` and `notebooks/`

---

## About Me

I am Emre Pelzer, a Data Science & AI graduate with a passion for data analysis and practical insights.  
This project is part of my public portfolio — feel free to [connect with me on LinkedIn](https://www.linkedin.com/in/emre-pelzer-b14148324).

---