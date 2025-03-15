from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from mongo_to_dag import replicate_data

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 3, 14),
    "retries": 1,
}

with DAG(
    "mongo_to_pg_replication",
    default_args=default_args,
    schedule_interval="@hourly",
    catchup=False,
) as dag:

    replicate_task = PythonOperator(
        task_id="replicate_mongo_to_pg",
        python_callable=replicate_data,
    )
