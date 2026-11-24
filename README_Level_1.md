# Codveda Technology – Data Analytics Internship

## Level 1 – Basic Data Analytics

### Organization
Codveda Technology

### Domain
Data Analytics

### Level
Level 1 – Basic

---

## 1. Project Overview

This project is part of the Codveda Technology Data Analytics Internship – Level 1.

The main objective is to understand and perform basic data analytics operations using Python. This level consists of two tasks:

1. Data Cleaning
2. Exploratory Data Analysis (EDA)

Both tasks use the Iris dataset.

---

## 2. Tasks Completed

### Task 1 – Data Cleaning

**Dataset:** `1) iris.csv`

**Python Script:** `scripts/task1_cleaning.py`

**Libraries Used:**
- Python
- Pandas
- NumPy

#### Methodology

The following data cleaning operations were performed:

1. Loaded the Iris dataset using Pandas.
2. Checked the dataset dimensions.
3. Identified duplicate records.
4. Checked missing values in all columns.
5. Removed duplicate records.
6. Standardized species category text.
7. Converted numerical columns into numeric data types.
8. Applied median imputation for numerical missing values, if present.
9. Removed rows with missing species values.
10. Exported the cleaned dataset as a CSV file.

#### Results

| Description | Result |
|---|---:|
| Original Rows | 150 |
| Original Columns | 5 |
| Duplicate Records Found | 3 |
| Missing Values | 0 |
| Duplicate Records Removed | 3 |
| Final Rows | 147 |
| Final Columns | 5 |
| Remaining Duplicates | 0 |

**Output File:** `outputs/iris_cleaned.csv`

The original dataset contained 3 duplicate records. These records were removed successfully. No missing values were found.

The final cleaned dataset contains 147 rows and 5 columns.

---

### Task 2 – Exploratory Data Analysis (EDA)

**Dataset:** `1) iris.csv`

**Python Script:** `scripts/task2_eda.py`

**Libraries Used:**
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

#### Methodology

The following exploratory data analysis operations were performed:

1. Loaded the Iris dataset.
2. Removed duplicate records for analysis.
3. Selected numerical features.
4. Calculated Mean, Median, Standard Deviation and Mode.
5. Created histograms to understand feature distributions.
6. Created a boxplot to compare petal length across species.
7. Created a scatter plot to examine the relationship between petal length and petal width.
8. Calculated the correlation matrix.
9. Created a correlation heatmap to visualize relationships between numerical features.
10. Exported statistical summaries and correlation results as CSV files.

#### Statistical Results

| Feature | Mean | Median | Standard Deviation | Mode |
|---|---:|---:|---:|---:|
| Sepal Length | 5.856463 | 5.8 | 0.829100 | 5.0 |
| Sepal Width | 3.055782 | 3.0 | 0.437009 | 3.0 |
| Petal Length | 3.780272 | 4.4 | 1.759111 | 1.4 |
| Petal Width | 1.208844 | 1.3 | 0.757874 | 0.2 |

#### Visualizations Created

The following seven visualizations were generated:

| No. | Visualization | Output File |
|---|---|---|
| 1 | Sepal Length Histogram | `eda_hist_sepal_length.png` |
| 2 | Sepal Width Histogram | `eda_hist_sepal_width.png` |
| 3 | Petal Length Histogram | `eda_hist_petal_length.png` |
| 4 | Petal Width Histogram | `eda_hist_petal_width.png` |
| 5 | Boxplot – Petal Length by Species | `eda_boxplot.png` |
| 6 | Scatter Plot – Petal Length vs Petal Width | `eda_scatter.png` |
| 7 | Feature Correlation Heatmap | `eda_correlation_heatmap.png` |

#### CSV Outputs

Two additional CSV files were generated:

- `iris_summary_statistics.csv` – Contains mean, median, standard deviation and mode for numerical features.
- `iris_correlation.csv` – Contains the correlation matrix of numerical features.

#### Key Findings

- The dataset contains four numerical features and one categorical feature.
- Petal length has a mean of approximately 3.78.
- Petal width has a mean of approximately 1.21.
- Histograms were used to examine feature distributions.
- Boxplots were used to compare petal length across species.
- Scatter plots were used to explore relationships between petal length and petal width.
- Correlation analysis was performed to examine relationships between numerical features.

---

## 3. Project Folder Structure

```text
Codveda_Data_Analytics_Internship/
│
├── datasets/
│   └── Data Set For Task/
│       └── 1) iris.csv
│
├── scripts/
│   ├── common.py
│   ├── task1_cleaning.py
│   └── task2_eda.py
│
├── outputs/
│   ├── iris_cleaned.csv
│   ├── iris_summary_statistics.csv
│   ├── iris_correlation.csv
│   ├── eda_hist_sepal_length.png
│   ├── eda_hist_sepal_width.png
│   ├── eda_hist_petal_length.png
│   ├── eda_hist_petal_width.png
│   ├── eda_boxplot.png
│   ├── eda_scatter.png
│   └── eda_correlation_heatmap.png
│
├── Level - 1/
│   ├── Task - 1 - Data - Cleaning/
│   └── Task-2-EDA/
│
├── Level - 2/
├── Level - 3/
│
├── README.md
├── README_Level_1.md
├── README_Level_2.md
├── README_Level_3.md
├── README_TAMIL.md
└── requirements.txt
```

---

## 4. How to Run the Project

### Step 1 – Activate Virtual Environment

```bash
.venv\Scripts\activate
```

### Step 2 – Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 3 – Run Data Cleaning

```bash
python scripts/task1_cleaning.py
```

### Step 4 – Run Exploratory Data Analysis

```bash
python scripts/task2_eda.py
```

The generated CSV files and visualizations are saved in the `outputs` folder.

---

## 5. Learning Outcomes

Through this project, the following skills were developed:

- Understanding dataset structure.
- Identifying and removing duplicate records.
- Checking and handling missing values.
- Cleaning and transforming data using Pandas.
- Performing descriptive statistical analysis.
- Understanding data distributions through histograms.
- Comparing categories using boxplots.
- Exploring relationships using scatter plots.
- Understanding correlation between numerical variables.
- Creating data visualizations using Matplotlib and Seaborn.
- Exporting processed datasets and analytical results into CSV files.

---

## 6. Conclusion

Level 1 of the Codveda Technology Data Analytics Internship was completed by performing Data Cleaning and Exploratory Data Analysis on the Iris dataset.

The data cleaning task successfully removed 3 duplicate records, producing a cleaned dataset containing 147 rows and 5 columns.

The EDA task generated statistical summaries, seven visualizations, and two CSV analytical outputs.

These tasks provided practical experience in data preprocessing, statistical analysis, and data visualization using Python.

---

**Internship:** Codveda Technology  
**Domain:** Data Analytics  
**Level:** Level 1 – Basic  
**Status:** Task 1 and Task 2 Completed