import logging

import random
from faker import Faker
import psycopg2
from psycopg2 import DatabaseError

# from connect import create_connect
Faker.seed(14)

fake = Faker()
COUNT = 200

conn = psycopg2.connect(host="localhost", 
                        port=5433, 
                        database="HomeWork 05", 
                        user="postgres", 
                        password="mypass")
cur=conn.cursor()

for _ in range(COUNT):
    cur.execute("INSERT INTO status (name) VALUES (%s)", (fake.word()))

for _ in range(COUNT):
    fullname = fake.name()
    email = fake.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

