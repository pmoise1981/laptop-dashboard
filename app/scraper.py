# app/scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

BASE_URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

def scrape_laptops():
    all_products = []
    for page in range(1, 5):
        url = f"{BASE_URL}?page={page}"
        res = requests.get(url)
        if res.status_code != 200:
            break

        soup = BeautifulSoup(res.text, "html.parser")
        products = soup.select("div.thumbnail")
        if not products:
            break

        for p in products:
            title_tag = p.select_one("a.title")
            price_tag = p.select_one("h4.price")
            desc_tag = p.select_one("p.description")
            review_tag = p.select_one("div.ratings > p.pull-right")

            all_products.append({
                "title": title_tag.get("title", "").strip() if title_tag else "",
                "price": float(price_tag.text.replace("$", "")) if price_tag else 0.0,
                "description": desc_tag.text.strip() if desc_tag else "",
                "reviews": int(review_tag.text.split()[0]) if review_tag else 0
            })
        time.sleep(1)

    return all_products

def save_to_csv(products):
    df = pd.DataFrame(products)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/products.csv", index=False)
    print(f" Saved {len(df)} products to data/products.csv")

if __name__ == "__main__":
    save_to_csv(scrape_laptops())

