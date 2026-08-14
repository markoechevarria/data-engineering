from airflow.decorators import dag, task
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime
import os

@dag(
    dag_id='get_files_s3_bucket',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=['aws', 's3']
)
def s3_process():

    @task
    def list_s3_files(bucket_name: str, aws_conn_id=None):
        hook = S3Hook(aws_conn_id=aws_conn_id)
        keys = hook.list_keys(bucket_name=bucket_name)
        return keys or []

    @task
    def download_files(keys: list, bucket_name: str, aws_conn_id=None):
        
        hook = S3Hook(aws_conn_id=aws_conn_id)
        
        local_directory = '/opt/airflow/data'
        os.makedirs(local_directory, exist_ok=True)
        
        for key in keys:
            print(f"Downloading {key}...")
            hook.download_file(
                key=key,
                bucket_name=bucket_name,
                local_path=local_directory,
                preserve_file_name=True
            )
        return local_directory

    BUCKET = 'airflow-bucket-input'

    file_keys = list_s3_files(bucket_name=BUCKET)
    download_files(keys=file_keys, bucket_name=BUCKET)

s3_process()
