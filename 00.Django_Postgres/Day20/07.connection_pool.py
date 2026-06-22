from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(
    1, 5,
    dbname="dvdrental",
    user="syedjaferk",
    password="qwerty123"
)

conn = connection_pool.getconn()
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM students")
print("Count:", cur.fetchone())

connection_pool.putconn(conn)