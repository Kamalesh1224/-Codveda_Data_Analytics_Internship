# Codveda Technology Internship – Level 3

## Advanced Data Analytics

### Organization
Codveda Technology

### Domain
Data Analytics

### Level
Level 3 – Advanced

---

## Project Overview

This repository contains the Level 3 tasks completed as part of the Codveda Technology Data Analytics Internship.

The objective of this level is to gain practical experience in machine learning classification and interactive data visualization.

The following two tasks were selected:

1. Classification
2. Tableau Public Dashboard

---

# Task 1 – Classification

## Dataset

Customer Churn Prediction Dataset

- churn-bigml-80.csv
- churn-bigml-20.csv

## Objective

To develop and evaluate machine learning classification models using customer churn data.

The goal is to identify customers who may leave a service and understand how machine learning can support customer retention analysis.

## Tools and Technologies

- Python
- Pandas
- Scikit-learn
- VS Code

## Methodology

1. Loaded the training and testing datasets.
2. Inspected the dataset features.
3. Prepared the input features and target variable.
4. Processed numerical and categorical data.
5. Trained Logistic Regression, Decision Tree, and Random Forest models.
6. Compared the performance of the models.
7. Evaluated the models using precision, recall, F1-score, accuracy, and confusion matrices.
8. Performed hyperparameter tuning.
9. Evaluated the best model on the test dataset.

## Model Accuracy Comparison

| Model | Accuracy |
|---|---:|
| Logistic Regression | 77.96% |
| Decision Tree | 92.05% |
| Random Forest | 95.35% |

## Best Model

Random Forest achieved the highest accuracy among the compared models.

### Best Model Test Results

| Metric | Class 0 | Class 1 |
|---|---:|---:|
| Precision | 0.96 | 0.84 |
| Recall | 0.98 | 0.78 |
| F1-Score | 0.97 | 0.81 |
| Support | 572 | 95 |

### Overall Performance

| Metric | Result |
|---|---:|
| Accuracy | 95.35% |
| Macro Average Precision | 0.90 |
| Macro Average Recall | 0.88 |
| Macro Average F1-Score | 0.89 |
| Weighted Average F1-Score | 0.95 |

### Confusion Matrix

```text
[[563   9]
 [ 22  73]]
```

### Best Model Parameters

```python
{
    'model__max_depth': None,
    'model__min_samples_split': 5,
    'model__n_estimators': 100
}
```

## Interpretation

The Random Forest model achieved the highest accuracy of approximately 95.35%.

It correctly classified most customers in the test dataset.

For the churn class (Class 1), the model achieved:

- Precision: 0.84
- Recall: 0.78
- F1-Score: 0.81

These results indicate that the model performed well overall, although some customers who actually churned were not identified.

## Learning Outcomes

- Understanding supervised machine learning.
- Preparing training and testing datasets.
- Comparing classification algorithms.
- Evaluating model performance.
- Understanding precision, recall, F1-score, and accuracy.
- Performing hyperparameter tuning.
- Applying machine learning to customer churn prediction.

---

# Task 2 – Tableau Public Dashboard

## Dataset

Sentiment dataset.csv

## Visualization Tool

Tableau Public

## Objective

To analyze sentiment data and present meaningful information through interactive visualizations and a dashboard.

## Methodology

1. Imported the sentiment dataset into Tableau Public.
2. Examined the available dataset fields.
3. Prepared the data for visualization.
4. Created suitable charts based on the dataset.
5. Organized the charts into a dashboard.
6. Published the dashboard using Tableau Public.

## Dashboard Link

**Tableau Public Dashboard:** 

[Add the published Tableau Public dashboard URL here]

## Learning Outcomes

- Understanding data visualization.
- Working with Tableau Public.
- Creating interactive dashboards.
- Presenting analytical insights.
- Communicating data findings visually.

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
│   ├── task7_classification.py
│   └── task9_sentiment.py
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

Open the project folder in VS Code.

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the classification script:

```bash
python scripts/task7_classification.py
```

Open the published Tableau Public dashboard using the dashboard link provided above.

---

## Conclusion

Level 3 provided practical experience in advanced data analytics through classification and dashboard development.

The classification task helped me understand how machine learning models can be trained and evaluated for customer churn prediction.

The Tableau Public task provided experience in creating and publishing interactive data visualizations.

---

**Internship Organization:** Codveda Technology  
**Domain:** Data Analytics  
**Level:** Level 3 – Advanced