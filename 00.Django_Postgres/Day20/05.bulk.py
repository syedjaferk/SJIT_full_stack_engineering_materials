from config import get_connection
from psycopg2.extras import execute_values

conn = get_connection()
cur = conn.cursor()

data = [(f"Student{i}", i % 30) for i in range(1000)]

execute_values(
    cur,
    "INSERT INTO students (name, age) VALUES %s",
    data
)

conn.commit()

print("Bulk insert completed")

cur.close()
conn.close()