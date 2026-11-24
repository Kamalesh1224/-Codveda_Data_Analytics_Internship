from common import *
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv(require(stock_path()), parse_dates=["date"])
# Select one symbol to avoid mixing different companies' prices.
symbol = "AAPL" if "AAPL" in set(df["symbol"]) else df["symbol"].iloc[0]
one = df[df["symbol"] == symbol].sort_values("date").set_index("date")
series = one["close"].resample("D").last().ffill()

plt.figure(figsize=(11, 4))
plt.plot(series)
plt.title(f"{symbol} daily closing price")
plt.xlabel("Date"); plt.ylabel("Close")
plt.tight_layout(); plt.savefig(OUT / "stock_timeseries.png", dpi=150); plt.close()

ma = series.rolling(window=30, min_periods=1).mean()
plt.figure(figsize=(11, 4))
plt.plot(series, alpha=.5, label="Daily close")
plt.plot(ma, label="30-day moving average")
plt.legend(); plt.title(f"{symbol}: 30-day moving average")
plt.tight_layout(); plt.savefig(OUT / "stock_moving_average.png", dpi=150); plt.close()

# Weekly frequency gives enough observations for a 52-week seasonal period.
weekly = one["close"].resample("W").last().ffill()
if len(weekly) >= 104:
    decomposition = seasonal_decompose(weekly, model="additive", period=52)
    fig = decomposition.plot()
    fig.set_size_inches(12, 8)
    fig.tight_layout()
    fig.savefig(OUT / "stock_decomposition.png", dpi=150)
else:
    print("Not enough weekly observations for 52-week decomposition.")
print("Selected symbol:", symbol, "| daily rows:", len(series), "| weekly rows:", len(weekly))
