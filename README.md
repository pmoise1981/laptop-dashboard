# 💻 Laptop Price Dashboard

An interactive web-based dashboard built with Flask, BeautifulSoup, and Plotly to visualize laptop product data scraped from a sample e-commerce site.

## 🚀 Features

- Scrapes product data (title, price, description, reviews) from the laptops category.
- Cleans and analyzes the data using `pandas`.
- Displays:
  - ✅ Total product count
  - ✅ Number of products under $100
  - ✅ Max price
  - ✅ Top 5 most frequent words in product titles
- Visualizes:
  - 📊 Price distribution
  - 📊 Review count distribution
  - 📊 Word frequency (bar chart)
- Interactive dashboard powered by Plotly and Flask.

## 📁 Project Structure

laptop_dashboard_project/
│
├── app/
│ ├── scraper.py # Scrapes laptop data and saves to CSV
│ ├── analysis.py # Loads + analyzes the scraped data
│ ├── dashboard.py # Flask app rendering the dashboard
│ └── templates/
│ └── dashboard.html # HTML + Plotly dashboard UI
│
├── data/
│ └── products.csv # Cleaned scraped data
│
├── requirements.txt # Python dependencies
├── Dockerfile # Container setup for deployment
└── README.md # Project overview 


---

## ⚙️ Installation & Run

### 🔧 1. Clone & Setup
```bash
git clone https://github.com/yourusername/laptop_dashboard_project.git
cd laptop_dashboard_project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. Scrape Product Data
python3 app/scraper.py

3. Start Dashboard
python3 app/dashboard.py

🐳 Docker (Optional)
To run with Docker:

docker build -t laptop-dashboard .
docker run -p 5000:5000 laptop-dashboard

Credits
Built with:

Flask

pandas

Plotly

BeautifulSoup

📌 Notes
Data source: webscraper.io test site

This project is for educational and portfolio use only

📬 Contact
Pierre Moise
📧 GitHub: @pmoise1981


