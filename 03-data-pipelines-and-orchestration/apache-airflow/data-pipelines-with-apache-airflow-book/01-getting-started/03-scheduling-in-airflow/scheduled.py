import datetime
from os import stat
from pathlib import Path

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
import pandas as pd

dag = DAG(
    dag_id="01_unscheduled",
    start_date=datetime.datetime(2019, 1,1),
    end_date=datetime.datetime(2019,1,5),
    schedule="@daily",
    catchup=False
)

fetch_events = BashOperator(
    task_id="fetch_events",
    bash_command=(
        "mkdir -p /data &&",
        "curl -o /data/event/{{ds}}.json ",
        "http://localhost:5000/events?",
        "start_date={{ds}}&", # execution_date.strftime('%Y-%m-%d')}}&"
        "end_date={{next_ds}}", # next_execution_date.strftime('%Y-%m-%d')}}"
    ),
    dag=dag
)

def _calculate_stats(**context):
    input_path = context["template_dict"]["input_path"]
    output_path = context["template_dict"]["output_path"]

    Path(output_path).parent.mkdir(exist_ok=True)

    events = pd.read_json(input_path)
    stats = events.groupby(["date", "user"]).size().reset_index()
    stats.to_csv(output_path, index=False)

calculate_stats = PythonOperator(
    task_id="calculate_stats",
    python_callable=_calculate_stats,
    templates_dict={
        "input_path": "/data/events/{{ds}}.json",
        "output_path": "/data/stats/{{ds}}.csv"
    },
    dag=dag
)

def _send_stats(email, **context):
    stats = pd.read_csv(context["templates_dict"]["stats_path"])
    email_stats(stats, email=email)

send_stats = PythonOperator(
    task_id="send_stats",
    python_callable=_send_stats,
    op_kwargs={"email": "marko@admin.com"},
    templates_dict={"stats_path": "/data/stats/{{ds}}.csv"},
    dag=dag
)

fetch_events >> calculate_stats >> send_stats

