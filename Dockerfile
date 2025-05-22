FROM python:3.11-slim

WORKDIR /app

# Copy project files
COPY app/ app/
COPY data/ data/
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run scraper then dashboard
CMD ["sh", "-c", "python3 app/scraper.py && python3 app/dashboard.py"]

