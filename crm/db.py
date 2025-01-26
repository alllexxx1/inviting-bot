import os
import sqlite3
from datetime import datetime

from configuration.logger import get_logger

logger = get_logger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQL_COMMANDS_FILE_PATH = os.path.join(BASE_DIR, 'crm', 'database.sql')
DB_PATH = os.path.join(BASE_DIR, 'crm', 'crm.db')


def fetch_sql_queries(sql_commands_file_path):
    queries = {}

    with open(sql_commands_file_path, "r") as file:
        sql = file.read()
        commands = sql.split("--")
        for command in commands:
            if command.strip():
                lines = command.strip().split("\n", 1)
                if len(lines) == 2:
                    query_name, query_body = lines
                    queries[query_name.strip()] = query_body.strip()

    return queries


SQL_QUERIES = fetch_sql_queries(SQL_COMMANDS_FILE_PATH)


def create_connection(database_url: str):
    connection = sqlite3.connect(database_url)
    return connection


def close_connection(connection):
    connection.close()


def init_db():
    conn = create_connection(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(SQL_QUERIES['Create table'])
        conn.commit()
        close_connection(conn)
    except Exception as e:
        logger.error(f'Failed to initiate data base: {e}')
    finally:
        close_connection(conn)


def add_user(user_tg_id, username, full_name):
    conn = create_connection(DB_PATH)
    cursor = conn.cursor()
    registered_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        cursor.execute(
            SQL_QUERIES['Insert user'],
            (user_tg_id, username, full_name, False, 1, registered_at)
        )
        conn.commit()
        close_connection(conn)
    except sqlite3.IntegrityError:
        logger.info('User already exists')
    close_connection(conn)


def drop_user(user_tg_id):
    conn = create_connection(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(SQL_QUERIES['Drop user'], (user_tg_id,))
        conn.commit()
        close_connection(conn)
    except Exception as e:
        logger.error(f'Failed to delete user {user_tg_id}: {e}')
    finally:
        close_connection(conn)


def fetch_users():
    conn = create_connection(DB_PATH)
    cursor = conn.cursor()
    try:
        users = cursor.execute(SQL_QUERIES['Fetch all users'])
        users = users.fetchall()
        conn.commit()
        close_connection(conn)
        return users
    except Exception as e:
        logger.error(f'Failed to fetch users: {e}')
    finally:
        close_connection(conn)


def fetch_user_db_id(user_tg_id):
    conn = create_connection(DB_PATH)
    cursor = conn.cursor()
    try:
        db_id = cursor.execute(SQL_QUERIES['Fetch user db id'], (user_tg_id,))
        db_id = db_id.fetchone()[0]
        conn.commit()
        close_connection(conn)
        return db_id
    except Exception as e:
        logger.error(f'Failed to fetch the user db id (tg_id – {user_tg_id}): {e}')
    finally:
        close_connection(conn)


def fetch_user_by_tg_id(user_tg_id):
    conn = create_connection(DB_PATH)
    cursor = conn.cursor()
    try:
        db_id = cursor.execute(SQL_QUERIES['Fetch user'], (user_tg_id,))
        db_id = db_id.fetchone()[0]
        conn.commit()
        close_connection(conn)
        return db_id
    except Exception as e:
        logger.error(f'Failed to fetch the user (tg_id – {user_tg_id}): {e}')
    finally:
        close_connection(conn)


def fetch_ineligible_users():
    conn = create_connection(DB_PATH)
    cursor = conn.cursor()
    try:
        users = cursor.execute(SQL_QUERIES['Fetch ineligible users'])
        result = users.fetchall()
        conn.commit()
        close_connection(conn)
        return result
    except Exception as e:
        logger.error(f'Failed to fetch ineligible users: {e}')
    finally:
        close_connection(conn)


def update_eligibility(user_tg_id):
    conn = create_connection(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(SQL_QUERIES['Update eligibility'], (True, user_tg_id))
        conn.commit()
        close_connection(conn)
    except Exception as e:
        logger.error(f'Failed to update eligibility for user {user_tg_id}: {e}')
    finally:
        close_connection(conn)


def update_reminder_count(user_tg_id):
    conn = create_connection(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(SQL_QUERIES['Update reminder count'], (0, user_tg_id))
        conn.commit()
        close_connection(conn)
    except Exception as e:
        logger.error(f'Failed to update reminder counter for user {user_tg_id}: {e}')
    finally:
        close_connection(conn)


def is_user_eligible(user_tg_id):
    conn = create_connection(DB_PATH)
    cursor = conn.cursor()
    try:
        eligibility = cursor.execute(SQL_QUERIES['Check eligibility'], (user_tg_id,))
        eligibility = eligibility.fetchone()[0]
        conn.commit()
        close_connection(conn)
        return eligibility
    except Exception as e:
        logger.error(f'Failed to check eligibility: {e}')
    finally:
        close_connection(conn)


def drop_table():
    conn = create_connection(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(SQL_QUERIES['Drop table'])
        conn.commit()
        close_connection(conn)
    except Exception as e:
        logger.error(f'Failed to drop the table: {e}')
    finally:
        close_connection(conn)


iu = fetch_ineligible_users()
for u in iu:
    print(u[6])
