from pymongo import MongoClient
import random
from datetime import datetime, timedelta

MONGO_URI = "mongodb://mongo_db:27017/"
client = MongoClient(MONGO_URI)
db = client["etl_database"]

def random_date(days=30):
    return datetime.now() - timedelta(days=random.randint(0, days))

def generate_sessions(n=500):
    return [
        {
            "session_id": str(random.randint(10000, 99999)),
            "user_id": random.randint(1, 100),
            "start_time": random_date(),
            "end_time": datetime.now(),
            "pages_visited": [f"/page_{random.randint(1, 50)}" for _ in range(random.randint(1, 10))],
            "device": random.choice(["mobile", "desktop", "tablet"]),
            "actions": [random.choice(["click", "scroll", "purchase", "add_to_cart"]) for _ in range(random.randint(1, 5))]
        }
        for _ in range(n)
    ]

def generate_product_price_history(n=200):
    return [
        {
            "product_id": i,
            "price_changes": [{"date": random_date().isoformat(), "price": round(random.uniform(10, 500), 2)} for _ in range(5)],
            "current_price": round(random.uniform(10, 500), 2),
            "currency": random.choice(["USD", "EUR", "RUB"])
        }
        for i in range(n)
    ]

def generate_event_logs(n=500):
    return [
        {
            "event_id": random.randint(10000, 99999),
            "timestamp": random_date(),
            "event_type": random.choice(["login", "logout", "purchase", "error"]),
            "details": f"Some event detail {random.randint(1, 100)}"
        }
        for _ in range(n)
    ]

def generate_support_tickets(n=300):
    return [
        {
            "ticket_id": random.randint(10000, 99999),
            "user_id": random.randint(1, 100),
            "status": random.choice(["open", "closed", "pending"]),
            "issue_type": random.choice(["payment", "technical", "account"]),
            "messages": [{"timestamp": random_date().isoformat(), "message": f"Message {i}"} for i in range(random.randint(1, 5))],
            "created_at": random_date(),
            "updated_at": datetime.now()
        }
        for _ in range(n)
    ]

def generate_user_recommendations(n=100):
    return [
        {
            "user_id": i,
            "recommended_products": [f"product_{random.randint(1, 200)}" for _ in range(5)],
            "last_updated": datetime.now()
        }
        for i in range(n)
    ]

def generate_moderation_queue(n=200):
    return [
        {
            "review_id": random.randint(10000, 99999),
            "user_id": random.randint(1, 100),
            "product_id": random.randint(1, 200),
            "review_text": f"Review {random.randint(1, 100)}",
            "rating": random.randint(1, 5),
            "moderation_status": random.choice(["pending", "approved", "rejected"]),
            "flags": [random.choice(["spam", "offensive", "duplicate"]) for _ in range(random.randint(0, 2))],
            "submitted_at": random_date()
        }
        for _ in range(n)
    ]

def generate_search_queries(n=300):
    """Генерирует поисковые запросы."""
    return [
        {
            "query_id": random.randint(10000, 99999),
            "user_id": random.randint(1, 100),
            "query_text": f"Search query {random.randint(1, 100)}",
            "timestamp": random_date(),
            "filters": {"category": random.choice(["electronics", "clothing", "books"])},
            "results_count": random.randint(0, 100)
        }
        for _ in range(n)
    ]

db["UserSessions"].delete_many({})
db["ProductPriceHistory"].delete_many({})
db["EventLogs"].delete_many({})
db["SupportTickets"].delete_many({})
db["UserRecommendations"].delete_many({})
db["ModerationQueue"].delete_many({})
db["SearchQueries"].delete_many({})

db["UserSessions"].insert_many(generate_sessions(500))
db["ProductPriceHistory"].insert_many(generate_product_price_history(200))
db["EventLogs"].insert_many(generate_event_logs(500))
db["SupportTickets"].insert_many(generate_support_tickets(300))
db["UserRecommendations"].insert_many(generate_user_recommendations(100))
db["ModerationQueue"].insert_many(generate_moderation_queue(200))
db["SearchQueries"].insert_many(generate_search_queries(300))

print("data was uploaded")
