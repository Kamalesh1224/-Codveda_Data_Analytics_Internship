from common import *
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline

# The supplied housing file is headerless: 13 predictors + MEDV target.
cols = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT","MEDV"]
df = pd.read_csv(require(house_path()), sep=r"\s+", header=None, names=cols, engine="python")
df = df.apply(pd.to_numeric, errors="coerce").dropna(subset=["MEDV"])

X, y = df[cols[:-1]], df["MEDV"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = make_pipeline(SimpleImputer(strategy="median"), LinearRegression())
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("R2:", round(r2_score(y_test, pred), 4))
print("MSE:", round(mean_squared_error(y_test, pred), 4))
reg = model.named_steps["linearregression"]
print("Intercept:", reg.intercept_)
print("Coefficients:")
print(pd.Series(reg.coef_, index=X.columns).sort_values(ascending=False))
pd.DataFrame({"actual": y_test, "predicted": pred}).to_csv(OUT / "housing_predictions.csv", index=False)

plt.figure()
plt.scatter(y_test, pred, alpha=.7)
plt.xlabel("Actual MEDV"); plt.ylabel("Predicted MEDV")
plt.title("Housing: actual vs predicted")
plt.tight_layout(); plt.savefig(OUT / "housing_actual_vs_predicted.png", dpi=150); plt.close()
