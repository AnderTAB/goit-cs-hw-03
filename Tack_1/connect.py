import psycopg2 
from contextlib import contextmanager

@contextmanager 
def create_connect(): 
    try:
        conn = psycopg2.connect(host="localhost", port=5433, database="HomeWork 05", user="postgres", password="mypass")
        try:
            yield conn 
        finally: 
            conn.close()
    except psycopg2.OperationalError:
        print("Connection failed")