from urllib import request
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

dag = DAG(
    dag_id="stocksense",
    start_date= datetime.now() - timedelta(days=1),
    schedule="@hourly"
)

def _get_data(output_path, execution_date, **context):
    year, month, day, hour, *_  = execution_date.timetuple()
    url = (
        "https:/dumps.wikimedia.org/other/pageviews"
        f"{year}/{year}-{month:0>2}/"
        f"pageviews-{year}{month:0>2}{day:0>2}-{hour:0>2}0000.gz"
    )
    request.urlretrieve(url, output_path)

get_date = PythonOperator(
    task_id="get_data",
    python_callable=_get_data,
    op_kwargs={ "output_path": "/tmp/wikipageviews.gz" },
    dag=dag
)

"""
def _get_data(year, month, day, hour, output_path, **_): 
    url = (
        "https:/dumps.wikimedia.org/other/pageviews"
        f"{year}/{year}-{month:0>2}/"
        f"pageviews-{year}{month:0>2}{day:0>2}-{hour:0>2}0000.gz"
    )
    request.urlretrieve(url, output_path)

get_data = PythonOperator( 
    task_id="get_data",
    python_callable=_get_data,
    op_kwargs={ 
        "year": "{{ execution_date.year }}",
        "month": "{{ execution_date.month }}",
        "day": "{{ execution_date.day }}",
        "hour": "{{ execution_date.hour }}",
        "output_path": "/tmp/wikipageviews.gz" 
    },
    dag=dag
)

### airflow tasks render [dag id] [task id] [desired execution date]

"""
