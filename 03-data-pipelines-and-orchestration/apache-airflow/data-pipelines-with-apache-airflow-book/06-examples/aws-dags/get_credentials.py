from airflow.hooks.base import BaseHook
from airflow.models import Variable
from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id="get_credentials",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["aws", "credentials"]
)
def get_credentials():

    @task
    def get_aws_credentials():
        try:
            conn = BaseHook.get_connection("connection-airflow-01")
            print( conn )
        except Exception as e:
            print(f"Error {e}")

    get_aws_credentials()

get_credentials()
