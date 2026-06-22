from config import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute(
    "INSERT INTO students (name, age) VALUES (%s, %s) RETURNING id",
    ("Charlie", 23)
)

new_id = cur.fetchone()[0]

conn.commit()

print("New ID:", new_id)

cur.close()
conn.close()