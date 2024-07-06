FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY Scores.txt /Scores.txt

EXPOSE 5000

CMD ["python", "MainScore.py"]