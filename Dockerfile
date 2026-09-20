FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "stock_web_scrapper.py"]
HEALTHCHECK CMD curl -f http://localhost:80/health || exit 1