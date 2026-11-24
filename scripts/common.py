from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datasets" / "Data Set For Task"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

def iris_path():
    return DATA / "1) iris.csv"

def stock_path():
    return DATA / "2) Stock Prices Data Set.csv"

def sentiment_path():
    return DATA / "3) Sentiment dataset.csv"

def house_path():
    return DATA / "4) house Prediction Data Set.csv"

def churn_train_path():
    return DATA / "Churn Prdiction Data" / "churn-bigml-80.csv"

def churn_test_path():
    return DATA / "Churn Prdiction Data" / "churn-bigml-20.csv"

def require(path):
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}\n"
            "Extract the supplied dataset ZIP and copy its 'Data Set For Task' folder "
            "into this project's datasets folder. See README_TAMIL.md."
        )
    return path
