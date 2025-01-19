-- Create table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    username TEXT,
    full_name TEXT,
    registered_at TEXT,
    is_eligible BOOLEAN DEFAULT FALSE
);

-- Drop table
DROP TABLE users;

-- Insert user
INSERT INTO users (user_id, username, full_name, registered_at, is_eligible)
VALUES (?, ?, ?, ?, ?);

-- Fetch all users
SELECT * FROM users;

-- Fetch user
SELECT * FROM users
WHERE user_id = ?;

-- Fetch eligible users
SELECT user_id FROM users
WHERE is_eligible = True;

-- Fetch ineligible users
SELECT user_id FROM users
WHERE is_eligible = False;

-- Drop user
DELETE FROM users
WHERE user_id = ?;

-- Check eligibility
SELECT is_eligible FROM users
WHERE user_id = ?;

-- Update eligibility
UPDATE users
SET is_eligible = ?
WHERE user_id = ?;
