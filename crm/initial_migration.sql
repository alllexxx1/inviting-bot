-- Create table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_tg_id INTEGER,
    username TEXT,
    full_name TEXT,
    is_eligible BOOLEAN DEFAULT FALSE,
    reminder_count INTEGER,
    registered_at TEXT
);
