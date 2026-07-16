FROM python:3.11-alpine
WORKDIR /app

COPY assets/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY cli.py query.py ./
ENTRYPOINT ["python", "-u", "cli.py"]