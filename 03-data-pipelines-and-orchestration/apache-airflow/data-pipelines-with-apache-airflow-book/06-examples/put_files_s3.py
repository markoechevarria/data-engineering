from airflow.decorators import dag, task
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime
from pathlib import Path
import os
import pandas as pd

@dag(
    dag_id='put_files_s3',
    start_date=datetime(2026,1,1),
    schedule=None,
    catchup=False,
    tags=['upload', 'aws', 's3']
)
def put_files_s3():

    @task
    def upload_files(file_path_list: list[str], bucket_name: str, aws_conn_id: str =None):

        hook = S3Hook(aws_conn_id=aws_conn_id)
        for path_str in file_path_list:
            path = Path(path_str)

            hook.load_file(
                filename=str(path),
                key=f"data/{path.name}",
                bucket_name=bucket_name,
                replace=True
            )

    @task
    def read_files(directory: str | None = None):
        base_path = Path(directory)

        files = [str(p) for p in base_path.rglob("*.csv") if p.is_file()]
        print(files)
        return files
    
    csvs = read_files("/opt/airflow/data")
    upload_files(csvs, 'airflow-bucket-output')

put_files_s3()
