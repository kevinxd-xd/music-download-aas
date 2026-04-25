FROM python:3.14-slim-trixie

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-w", "1", "--access-logfile=-", "-b", "0.0.0.0", "flaskr.main:app"]