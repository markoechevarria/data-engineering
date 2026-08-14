from airflow.decorators import dag, task
from airflow.models import Variable
from airflow.operators.python import get_current_context
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import logging
import json
import uuid

@dag(
    dag_id='weather_pipeline_ingestion',
    start_date=datetime(2026,1,1),
    schedule='@daily',
    catchup=True,
    tags=['weather','etl'],
    default_args={
        'retries':3,
        'retry_delay':timedelta(seconds=3),
    }
)
def weather_pipeline():

    @task
    def get_weather_data():

        log = logging.getLogger(__name__)
        context = get_current_context()
        
        httpHook = HttpHook(http_conn_id='open-meteo-conn-config', method='GET')
        s3Hook = S3Hook(aws_conn_id=None)

        date_str = context['ds']
        start_date = datetime.strptime(date_str, "%Y-%m-%d")
        end_date = start_date + timedelta(days=2)

        parameters = {
            "latitude": float(Variable.get('latitude')),
            "longitude": float(Variable.get('longitude')),
            "start_date": start_date.strftime('%Y-%m-%d'),
            "end_date": end_date.strftime('%Y-%m-%d'),
            "start_hour": f"{date_str}T12:00",
            "end_hour": f"{date_str}T12:00",
            "hourly": "temperature_2m"
        }

        response = httpHook.run(endpoint='/v1/forecast', data=parameters)
        response.raise_for_status()

        path_file = f"raw/raw_data-{uuid.uuid4()}.json"
        s3Hook = s3Hook.load_string(
            string_data= response.text,
            key= path_file,
            bucket_name="raw-data-airflow-may",
            replace=True
        )

        log.info(f"Weather data fetched and saved as {path_file}")
        return path_file
    
    @task 
    def transform_weather(path_file):
        
        log = logging.getLogger(__name__)
        s3Hook = S3Hook(aws_conn_id=None)

        temp_local_path = Variable.get('temp_local_path')

        local_path = s3Hook.download_file(
            key=path_file,
            bucket_name='raw-data-airflow-may',
            local_path=temp_local_path
        )

        data = json.load(local_path)

        if 'hourly' not in data: raise ValueError("Invalid API response")

        transformed = {
            "latitude": data["latitude"],
            "longitude": data["longitude"],
            "time": data["hourly"]["time"][0].split('T')[0],
            "temperature_unit": data['hourly_units']['temperature_2m'],
            "temperature": data["hourly"]["temperature_2m"][0]
        }

        log.info("Weather transformed", extra={
            "date": transformed["time"],
            "lat": transformed["latitude"],
            "lon": transformed["longitude"]
        })

        name_tmp_file = f"tmp/tmp_data-{uuid.uuid4()}"
        s3Hook = s3Hook.load_string(
            string_data= transformed ,
            key= name_tmp_file,
            bucket_name="temp-data-airflow-may",
            replace=True
        )

        return name_tmp_file 

    @task
    def save_local_data_lake(data):

        log = logging.getLogger(__name__)
        context = get_current_context()
        s3Hook = S3Hook(aws_conn_id=None)

        if not data: return "No data received"
        base_dir = Variable.get('weather_base_path')
        
        record_date = data['time']
        dt = datetime.strptime(record_date, "%Y-%m-%d")
        
        run_id = context["run_id"]

        final_path = Path(base_dir) / f'year={dt.year}' / f"month={dt.strftime('%m')}" / f"day={dt.strftime('%d')}" / f"run={run_id}"
        final_path.mkdir( parents=True, exist_ok=True )

        file_name = f'{record_date}.parquet'
        final_path = final_path / file_name
        if final_path.exists():
            log.warning(f"File already exists: {file_name}")
            return str(final_path)
        
        df = pd.DataFrame([data])
        df.to_parquet(final_path)

        name_tmp_file = f"-{uuid.uuid4()}"
        s3Hook = s3Hook.load_string(
            string_data= transformed ,
            key= name_tmp_file,
            bucket_name="temp-data-airflow-may",
            replace=True
        )

        log.info(f"Saved: {final_path}")
        return f"{final_path}"
    
    @task
    def validate_file(path: str):
        if not Path(path).exists():
            raise FileNotFoundError(path)
        
        df = pd.read_parquet(path)

        if Path(path).stat().st_size == 0 or df.size == 0:
            raise ValueError('Empty file')
        
    raw = get_weather_data()
    transformed = transform_weather(raw) 
    #processed = save_local_data_lake(transformed)
    #validate_file(processed)

weather_pipeline()
