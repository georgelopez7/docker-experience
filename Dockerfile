FROM python:3.9

ADD football-scraper.py .

RUN pip install requests pandas fuzzywuzzy

CMD ["python", "./football-scraper.py"]