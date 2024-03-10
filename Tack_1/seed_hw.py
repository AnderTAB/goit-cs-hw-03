import random
from faker import Faker
import psycopg2
from psycopg2 import DatabaseError

from connect import db_config

fake = Faker()

def generate_users(n = 25):
    users = [(fake.name(), fake.unique.email()) for _ in range(n)]
    return users

def generate_statuses():
    statuses = [('new',), ('in progres',), ('completed',)]
    return statuses

def ganerate_tasks(n = 30):
    tasks = []
    for _ in range(n):
        title = fake.sentence(nb_words=6)
        description=fake.text(max_nb_chars=200)
        status_id = random.randint(1, 3)
        user_id = random.randint(1, 25)
        tasks.append((title, description, status_id, user_id))
    return tasks


def populate_database():
    conn=None
    try:
        conn = psycopg2.connect(**db_config)

        cur=conn.cursor()

        users= generate_users()
        cur.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s)", users)

        statuses= generate_statuses()
        cur.executemany("INSERT INTO status (name) VALUES (%s)", statuses)

        tasks= ganerate_tasks()
        cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", tasks)

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__=="__main__":
    populate_database()

