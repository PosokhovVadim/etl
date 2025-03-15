from pymongo import MongoClient
import psycopg2

def replicate_data():
    client = MongoClient("mongodb://mongo_db:27017/")
    db = client["etl_database"]
    conn = psycopg2.connect(
        dbname="airflow_db",
        user="airflow",
        password="airflow",
        host="postgres",
    )
    cursor = conn.cursor()
    
    cursor.execute("TRUNCATE TABLE user_sessions")  

    for session in db["UserSessions"].find():
        cursor.execute(
            "INSERT INTO user_sessions (session_id, user_id, start_time, end_time, device) VALUES (%s, %s, %s, %s, %s)",
            (session["session_id"], session["user_id"], session["start_time"], session["end_time"], session["device"]),
        )

    conn.commit()
    cursor.close()
    conn.close()

