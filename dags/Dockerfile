FROM apache/airflow:2.7.3-python3.10

COPY requirements.txt /opt/airflow/requirements.txt

USER airflow
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

USER root
COPY . /opt/airflow/dags

RUN chown -R airflow /opt/airflow/dags

USER airflow

CMD ["airflow", "scheduler"]
