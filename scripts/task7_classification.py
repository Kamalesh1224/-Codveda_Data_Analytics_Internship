from common import *
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.compose import make_column_selector

train = pd.read_csv(require(churn_train_path()))
test = pd.read_csv(require(churn_test_path()))
target = "Churn"
X_train, y_train = train.drop(columns=[target]), train[target].astype(int)
X_test, y_test = test.drop(columns=[target]), test[target].astype(int)

cat_cols = X_train.select_dtypes(include=["object", "bool"]).columns.tolist()
num_cols = X_train.select_dtypes(include="number").columns.tolist()
preprocess = ColumnTransformer([
    ("num", Pipeline([("imputer", SimpleImputer(strategy="median")),
                      ("scale", StandardScaler())]), num_cols),
    ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),
                      ("onehot", OneHotEncoder(handle_unknown="ignore"))]), cat_cols)
])

models = {
    "LogisticRegression": LogisticRegression(max_iter=2000, class_weight="balanced"),
    "DecisionTree": DecisionTreeClassifier(random_state=42, class_weight="balanced"),
    "RandomForest": RandomForestClassifier(random_state=42, class_weight="balanced")
}
rows = []
for name, estimator in models.items():
    pipe = Pipeline([("prep", preprocess), ("model", estimator)])
    pipe.fit(X_train, y_train)
    pred = pipe.predict(X_test)
    rows.append({"model": name, "accuracy": accuracy_score(y_test, pred)})
    print("\n", name, "\n", classification_report(y_test, pred, zero_division=0))
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))

print("\nModel accuracy comparison:\n", pd.DataFrame(rows))
# Grid search example on Random Forest; training data only.
rf_pipe = Pipeline([("prep", preprocess),
                    ("model", RandomForestClassifier(random_state=42, class_weight="balanced"))])
grid = GridSearchCV(
    rf_pipe,
    {"model__n_estimators": [100, 200],
     "model__max_depth": [None, 10, 20],
     "model__min_samples_split": [2, 5]},
    cv=5, scoring="f1", n_jobs=-1
)
grid.fit(X_train, y_train)
best_pred = grid.best_estimator_.predict(X_test)
print("\nBest params:", grid.best_params_)
print("Best model test report:\n", classification_report(y_test, best_pred, zero_division=0))
pd.DataFrame(rows).to_csv(OUT / "churn_model_comparison.csv", index=False)
