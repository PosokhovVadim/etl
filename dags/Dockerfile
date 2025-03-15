FROM apache/airflow:2.6.3

USER root
RUN pip install --no-cache-dir pymongo psycopg2-binary

WORKDIR /opt/airflow
COPY . /opt/airflow/dags

RUN chown -R airflow:airflow /opt/airflow

USER airflow

CMD ["airflow", "scheduler"]
