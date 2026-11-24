from common import *
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS

df = pd.read_csv(require(sentiment_path()))
df["Text"] = df["Text"].fillna("").astype(str)
df["clean_text"] = (df["Text"].str.lower()
                    .str.replace(r"http\S+|www\S+", " ", regex=True)
                    .str.replace(r"[^a-zA-Z\s]", " ", regex=True)
                    .str.replace(r"\s+", " ", regex=True).str.strip())

def classify(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.05: return "Positive"
    if polarity < -0.05: return "Negative"
    return "Neutral"

df["predicted_sentiment"] = df["clean_text"].apply(classify)
df.to_csv(OUT / "sentiment_scored.csv", index=False)
print("Provided label counts:\n", df["Sentiment"].value_counts())
print("TextBlob prediction counts:\n", df["predicted_sentiment"].value_counts())

plt.figure()
sns.countplot(data=df, x="predicted_sentiment", order=["Positive", "Neutral", "Negative"])
plt.title("TextBlob sentiment distribution")
plt.tight_layout(); plt.savefig(OUT / "sentiment_distribution.png", dpi=150); plt.close()

text = " ".join(df["clean_text"])
cloud = WordCloud(width=1200, height=600, background_color="white",
                  stopwords=STOPWORDS, collocations=False).generate(text or "No text")
cloud.to_file(str(OUT / "sentiment_wordcloud.png"))
