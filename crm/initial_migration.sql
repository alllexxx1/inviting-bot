-- Drop table
DROP TABLE IF EXISTS users;

-- Create table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    username TEXT,
    full_name TEXT,
    registered_at TEXT,
    is_eligible BOOLEAN DEFAULT FALSE
);
