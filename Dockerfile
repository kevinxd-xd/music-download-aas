FROM python:3.14-slim-trixie

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-w", "1", "--access-logfile=-", "-b", "0.0.0.0", "flaskr.main:app"]