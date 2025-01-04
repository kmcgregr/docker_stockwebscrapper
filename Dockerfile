FROM python:3
RUN python -m pip install --upgrade pip
RUN pip install bs4
RUN pip install requests
RUN pip install pandas
RUN pip install numpy
RUN pip install openpyxl
RUN pip install schedule

WORKDIR /usr/src/app

CMD ["python", "/usr/src/app/stock_web_scrapper.py"]