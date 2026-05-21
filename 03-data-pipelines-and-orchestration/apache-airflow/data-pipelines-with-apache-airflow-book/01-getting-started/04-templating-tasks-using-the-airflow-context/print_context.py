from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

dag = DAG(
    dag_id="print_context",
    start_date=datetime.now(),
    schedule="@once"
)

def _print_context(**kwargs):
    print(kwargs)

print_context = PythonOperator(
    task_id="print_context",
    python_callable=_print_context,
    dag=dag
)
