FROM python:3.14-slim-trixie

RUN useradd --create-home appuser
WORKDIR /home/appuser/app
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_24.x | bash - && \
    apt-get install -y nodejs

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 8000

CMD ["gunicorn", "-w", "1", "--access-logfile=-", "-b", "0.0.0.0", "flaskr.main:app"]