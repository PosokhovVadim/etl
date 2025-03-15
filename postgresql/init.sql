CREATE TABLE user_sessions (
    session_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    pages_visited JSONB,
    device VARCHAR NOT NULL,
    actions JSONB
);

CREATE TABLE product_price_history (
    product_id BIGINT PRIMARY KEY,
    price_changes JSONB,
    current_price NUMERIC(10, 2) NOT NULL,
    currency VARCHAR(10) NOT NULL
);

CREATE TABLE event_logs (
    event_id BIGINT PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    event_type VARCHAR NOT NULL,
    details TEXT
);

CREATE TABLE support_tickets (
    ticket_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    status VARCHAR NOT NULL,
    issue_type VARCHAR NOT NULL,
    messages JSONB,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

CREATE TABLE user_recommendations (
    user_id BIGINT PRIMARY KEY,
    recommended_products JSONB,
    last_updated TIMESTAMP NOT NULL
);

CREATE TABLE moderation_queue (
    review_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    review_text TEXT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    moderation_status VARCHAR NOT NULL,
    flags JSONB,
    submitted_at TIMESTAMP NOT NULL
);

CREATE TABLE search_queries (
    query_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    query_text TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    filters JSONB,
    results_count INT NOT NULL
);
