# Codveda Technology Internship – Level 2

## Intermediate Data Analytics

### Organization
Codveda Technology

### Domain
Data Analytics

### Level
Level 2 – Intermediate

---

## Project Overview

This repository contains the Level 2 tasks completed as part of the Codveda Technology Data Analytics Internship.

The main objective of this level is to gain practical experience in time series analysis and unsupervised machine learning.

The following two tasks were selected and completed:

1. Time Series Analysis
2. K-Means Clustering

---

# Task 1 – Time Series Analysis

## Dataset
Stock Prices Data Set.csv

## Objective

To analyze historical stock market data and understand stock price patterns over time using time series analysis techniques.

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- VS Code

## Methodology

1. Loaded the stock prices dataset.
2. Inspected the dataset and its structure.
3. Selected the AAPL stock symbol for analysis.
4. Prepared daily stock price records.
5. Resampled the daily data into weekly records.
6. Examined stock price information over time.
7. Generated the analysis outputs.

## Execution Results

The script executed successfully.

| Metric | Result |
|---|---:|
| Selected Stock Symbol | AAPL |
| Daily Records | 1,458 |
| Weekly Records | 209 |
| Execution Status | Successful |

## Learning Outcomes

- Understanding time series datasets.
- Working with stock market data.
- Understanding daily and weekly data frequencies.
- Learning how to prepare date-based datasets.
- Developing practical data analysis skills.

---

# Task 2 – K-Means Clustering

## Dataset
Iris Dataset – 1) iris.csv

## Objective

To apply the K-Means clustering algorithm to group similar Iris flower records based on their numerical features.

## Tools and Technologies

- Python
- Pandas
- Scikit-learn
- VS Code

## Methodology

1. Loaded the Iris dataset.
2. Selected the numerical features.
3. Prepared the dataset for clustering.
4. Applied the K-Means clustering algorithm.
5. Created three clusters.
6. Calculated the cluster centers.
7. Examined the feature values of each cluster.

## Execution Results

The clustering script executed successfully and generated three clusters.

### Cluster Centers

| Cluster | Sepal Length | Sepal Width | Petal Length | Petal Width |
|---|---:|---:|---:|---:|
| Cluster 0 | 5.801923 | 2.673077 | 4.355769 | 1.403846 |
| Cluster 1 | 5.010417 | 3.431250 | 1.462500 | 0.250000 |
| Cluster 2 | 6.780851 | 3.095745 | 5.510638 | 1.972340 |

## Learning Outcomes

- Understanding unsupervised machine learning.
- Learning the K-Means clustering algorithm.
- Grouping similar data points.
- Understanding cluster centers.
- Interpreting clustering results.

---

## Additional Practice

In addition to the two selected Level 2 tasks, I also executed a regression analysis script using the house prediction dataset.

### Linear Regression Results

| Metric | Result |
|---|---:|
| R² Score | 0.6688 |
| Mean Squared Error | 24.2911 |

This additional exercise provided practical experience in regression modeling and model evaluation.

---

## Project Structure

```text
Codveda_Data_Analytics_Internship/
│
├── datasets/
├── Level - 1/
├── Level - 2/
├── Level - 3/
├── outputs/
│
├── scripts/
│   ├── common.py
│   ├── task3_visualization.py
│   ├── task4_regression.py
│   ├── task5_timeseries.py
│   └── task6_clustering.py
│
├── README.md
├── README_Level_1.md
├── README_Level_2.md
├── README_Level_3.md
├── README_TAMIL.md
└── requirements.txt
```

---

## How to Run

Open the project folder in VS Code and activate the virtual environment.

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run Time Series Analysis:

```bash
python scripts/task5_timeseries.py
```

Run K-Means Clustering:

```bash
python scripts/task6_clustering.py
```

---

## Conclusion

Level 2 provided practical experience in time series analysis and unsupervised machine learning.

The stock price analysis helped me understand daily and weekly stock records, while K-Means clustering helped me understand how similar data points can be grouped using machine learning.

The additional regression exercise also strengthened my understanding of predictive modeling.

---

**Internship Organization:** Codveda Technology  
**Domain:** Data Analytics  
**Level:** Level 2 – Intermediate