# Codveda Data Analytics Internship – Starter Project

## Platform recommendation
Windows + Python 3.11 + VS Code (or Jupyter Notebook). Use VS Code for scripts/GitHub and Jupyter for exploration. Power BI Desktop is needed only for Level 3 Task 2.

## Folder setup
1. Extract this project folder.
2. Extract the supplied `Data Set For Task-....zip`.
3. Copy the extracted `Data Set For Task` folder into this project's `datasets` folder.
4. Expected paths:
   - `datasets/Data Set For Task/1) iris.csv`
   - `datasets/Data Set For Task/2) Stock Prices Data Set.csv`
   - `datasets/Data Set For Task/3) Sentiment dataset.csv`
   - `datasets/Data Set For Task/4) house Prediction Data Set.csv`
   - `datasets/Data Set For Task/Churn Prdiction Data/churn-bigml-80.csv`
   - `datasets/Data Set For Task/Churn Prdiction Data/churn-bigml-20.csv`

## Windows setup (PowerShell terminal in VS Code)
```powershell
py -3.11 --version
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
If PowerShell blocks activation, run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```
Alternative CMD activation: `.venv\Scripts\activate.bat`

## Run a task
From the project root:
```powershell
python scripts\task1_cleaning.py
python scripts\task2_eda.py
python scripts\task3_visualization.py
python scripts\task4_regression.py
python scripts\task5_timeseries.py
python scripts\task6_clustering.py
python scripts\task7_classification.py
python scripts\task9_sentiment.py
```
Outputs are saved in `outputs/`. Task 8 is completed in Power BI Desktop; follow the guide below.

## Dataset mapping / important observations
- Iris (150 rows, 5 columns): Level 1 Tasks 1–3 and Level 2 clustering. It has 3 exact duplicate rows and no missing values.
- Stock Prices (497,472 rows, 7 columns): Level 2 time-series. `open`, `high`, `low` contain 11, 8, 8 missing values respectively; parse `date` and filter one symbol before decomposition.
- House Prediction CSV (505 rows, 1 parsed column): Level 2 regression. The supplied file has no header row; script assigns Boston Housing-style 14 column names. Target is `MEDV`.
- Sentiment (732 rows, 15 columns): Level 3 NLP and can also be used in Power BI. Text and sentiment columns are present.
- Churn train (2,666 rows) + test (667 rows): Level 3 classification. Use the supplied 80/20 split as train/test. No missing values or duplicate rows in either file.

## Level selection
The instruction PDF says to complete any TWO tasks per level. That means plan for 2 tasks in Level 1, 2 in Level 2, and 2 in Level 3 (6 total), unless your coordinator gives a different interpretation.
Suggested manageable portfolio:
- Level 1: Task 1 Cleaning + Task 2 EDA (Task 3 is a good alternative).
- Level 2: Task 2 Time Series + Task 3 Clustering. Choose regression instead of clustering if your mentor specifically expects prediction.
- Level 3: Task 1 Churn Classification + Task 2 Power BI Dashboard. Task 3 NLP is a strong alternative.

## Task 8 – Power BI quick guide
1. Open Power BI Desktop → Get Data → Text/CSV.
2. Import `datasets/Data Set For Task/3) Sentiment dataset.csv`.
3. In Power Query: remove `Unnamed: 0` and `Unnamed: 0.1`; set `Timestamp` to Date/Time; check blank rows.
4. Create visuals: sentiment count (bar/donut), sentiment by Platform (stacked bar), posts over time (line), country distribution (bar/map if geographic values are suitable), likes and retweets by sentiment (clustered column).
5. Add slicers for Platform, Country, Sentiment, Year.
6. Add cards for total posts, average Likes, average Retweets.
7. Save as `outputs/Codveda_Sentiment_Dashboard.pbix`.
8. Publish only if you have an eligible Power BI account/workspace and permission to share the data.

## Submission checklist from the instruction PDF
- Keep a separate folder/file for each level.
- Submit using the Codveda submission form when they share it; PDF says the form will be shared later.
- Make a professional project explanation video and post it on LinkedIn with the GitHub repository link; tag Codveda and use relevant hashtags such as #CodvedaJourney, #CodvedaExperience, #FutureWithCodveda, #CodvedaAchievements, #CodvedaProjects.
- Update LinkedIn with achievements/offer letter/completion certificate as appropriate. Do not post private personal details from documents.
- The PDF specifies a one-month allocation. Confirm your exact deadline with the coordinator.
