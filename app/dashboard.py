from flask import Flask, render_template, request
import pandas as pd
from collections import Counter
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

# Load CSV data
df = pd.read_csv("data/products.csv")
df["title"] = df["title"].str.strip()
df["description"] = df["description"].str.strip()

@app.route("/", methods=["GET", "POST"])
def dashboard():
    max_price = request.form.get("max_price", type=float)
    filtered_df = df[df["price"] <= max_price] if max_price else df

    # Summary stats
    cheap_count = len(filtered_df[filtered_df["price"] < 100])
    words = []
    for title in filtered_df["title"]:
        words.extend(title.split())
    skip_words = {"the", "and", "with", "for", "a", "of", "in"}
    filtered_words = [w for w in words if w.lower() not in skip_words]
    word_counts = Counter(filtered_words).most_common(5)
    max_p = filtered_df["price"].max()

    # Charts
    price_chart = pio.to_html(
        px.histogram(filtered_df, x="price", nbins=20, title="💸 Price Distribution", template="plotly_dark"),
        include_plotlyjs='cdn', full_html=False
    )
    review_chart = pio.to_html(
        px.histogram(filtered_df, x="reviews", nbins=10, title="🗣️ Reviews Distribution", template="plotly_dark"),
        include_plotlyjs=False, full_html=False
    )

    return render_template(
        "dashboard.html",
        total=len(filtered_df),
        cheap=cheap_count,
        max_price=max_p,
        top_words=word_counts,
        selected_max=max_price or "",
        price_chart=price_chart,
        review_chart=review_chart,
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

