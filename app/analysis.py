# app/analysis.py
import pandas as pd
from collections import Counter

def load_data():
    return pd.read_csv("data/products.csv")

def analyze_data(df):
    df['title'] = df['title'].str.strip()
    df['description'] = df['description'].str.strip()

    under_100 = len(df[df['price'] < 100])
    max_price = df['price'].max()

    words = []
    for title in df['title']:
        words.extend(title.split())
    stop_words = {"the", "and", "for", "a", "of", "with", "in"}
    filtered = [w for w in words if w.lower() not in stop_words]
    freq_words = Counter(filtered).most_common(5)

    return under_100, max_price, freq_words

