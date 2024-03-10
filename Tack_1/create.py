import logging
from psycopg2 import DatabaseError
from connect import create_connect

def create_table(conn, sql_stmt_list):
    c = conn.cursor()
    try:
        for sql_stmt in sql_stmt_list:
            c.execute(sql_stmt)
        conn.commit()
    except DatabaseError as err:
        logging.error(f"Database error: {err}")
        conn.rollback()
    finally:
        c.close()

if __name__ =="__main__":
    sql_stmt = [
        """
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            fullname VARCHAR(120) NOT NULL UNIQUE,
            email VARCHAR(100) UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS status (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            description TEXT,
            status_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (status_id) REFERENCES status(id),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE      
        )
        """
    ]

    try:
        with create_connect() as conn:
            create_table(conn, sql_stmt)
    except RuntimeError as err:
        logging.error(f"Runtime error: {err}")
    except DatabaseError as err:
        logging.error(f"Database error: {err}")