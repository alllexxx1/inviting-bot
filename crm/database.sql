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

-- Drop table
DROP TABLE users;

-- Insert user
INSERT INTO users (user_tg_id, username, full_name, is_eligible, reminder_count, registered_at)
VALUES (?, ?, ?, ?, ?, ?);

-- Fetch all users
SELECT * FROM users;

-- Fetch user
SELECT * FROM users
WHERE user_tg_id = ?;

-- Fetch user db id
SELECT id FROM users
WHERE user_tg_id = ?;

-- Fetch eligible users
SELECT user_tg_id FROM users
WHERE is_eligible = True;

-- Fetch ineligible users
SELECT * FROM users
WHERE is_eligible = False;

-- Drop user
DELETE FROM users
WHERE user_tg_id = ?;

-- Check eligibility
SELECT is_eligible FROM users
WHERE user_tg_id = ?;

-- Update eligibility
UPDATE users
SET is_eligible = ?
WHERE user_tg_id = ?;

-- Update reminder count
UPDATE users
SET reminder_count = ?
WHERE user_tg_id = ?;
