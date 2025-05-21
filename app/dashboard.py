# app/dashboard.py
from flask import Flask, render_template
import pandas as pd
from analysis import load_data, analyze_data

app = Flask(__name__)

@app.route("/")
def home():
    df = load_data()
    under_100, max_price, top_words = analyze_data(df)
    return render_template("index.html", total=len(df), under_100=under_100, max_price=max_price, top_words=top_words)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

