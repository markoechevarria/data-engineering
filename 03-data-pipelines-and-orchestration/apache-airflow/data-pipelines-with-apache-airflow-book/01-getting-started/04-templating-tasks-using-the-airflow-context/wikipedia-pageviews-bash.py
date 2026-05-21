from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator

dag = DAG(
    dag_id="wikipedia-pageviews",
    start_date= datetime.now() - timedelta(days=3),
    schedule="@hourly"
)

get_data = BashOperator(
    task_id="get_data",
    bash_command=(
        "curl -o /tmp/wikipageviews.gz",
        "https://dumps.wikimedia.org/other/pageviews/",
        "{{ execution_date.year }}/",
        "{{ execution_date.year }}-",
        "{{ '{:02}'.format(execution_date.month) }}/",
        "pageviews-{{ execution_date.year }}"
        "{{ '{:02}'.format(execution_date.month) }}",
        "{{ '{:02}'.format(execution_date.day) }}-",
        "{{ '{:02}'.format(execution_date.hour) }}0000.gz"
    ),
    dag=dag
)
