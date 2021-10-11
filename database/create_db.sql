CREATE TABLE IF NOT EXISTS accounts (
    id serial PRIMARY KEY,
    name VARCHAR NOT NULL,
    document VARCHAR NOT NULL,
    born_date DATE NOT NULL,
    email VARCHAR NOT NULL,
    phone_number VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT current_timestamp,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS hellos (
    name VARCHAR,
    timestamp TIMESTAMP
);
