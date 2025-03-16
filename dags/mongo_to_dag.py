from pymongo import MongoClient
import psycopg2
import json

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

    tables = {
        "UserSessions": "user_sessions",
        "ProductPriceHistory": "product_price_history",
        "EventLogs": "event_logs",
        "SupportTickets": "support_tickets",
        "UserRecommendations": "user_recommendations",
        "ModerationQueue": "moderation_queue",
        "SearchQueries": "search_queries"
    }

    for collection, table in tables.items():
        print(f"🔄 Репликация {collection} → {table}")

        cursor.execute(f"TRUNCATE TABLE {table} RESTART IDENTITY;")
        for doc in db[collection].find():
            columns = ", ".join(doc.keys())
            values = [json.dumps(v) if isinstance(v, (dict, list)) else v for v in doc.values()]
            placeholders = ", ".join(["%s"] * len(values))

            insert_query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor.execute(insert_query, values)

        conn.commit()
        print(f"Replication {collection} has done!")

    cursor.close()
    conn.close()
