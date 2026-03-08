FROM python:3.11-slim
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app

CMD ["python", "-u", "stock_web_scrapper.py"]
HEALTHCHECK CMD curl -f http://localhost:80/health || exit 1
