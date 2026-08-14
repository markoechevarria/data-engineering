FROM apache/airflow:2.10.3-python3.11

ENV PIP_NO_CACHE_DIR=true

COPY requirements.txt .
COPY webserver_config.py .

RUN pip install -r requirements.txt
