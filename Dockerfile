FROM python:3.11-slim
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src
COPY config.yaml .
COPY stockwebscrapper/ ./stockwebscrapper
CMD ["python", "-u", "-m", "src.main", "schedule"]
