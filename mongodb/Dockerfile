FROM python:3.10-slim

WORKDIR /app
COPY data_gen.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r /app/requirements.txt

ENV MONGO_URI="mongodb://mongo_db:27017/"

CMD ["python", "data_gen.py"]
