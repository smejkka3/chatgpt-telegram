DROP TABLE IF EXISTS history;
CREATE TABLE history (
    id SERIAL PRIMARY KEY,
    chat_id character varying(255) NOT NULL,
    user_id character varying(255) NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);