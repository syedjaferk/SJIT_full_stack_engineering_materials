from config import get_connection

conn = get_connection()
cur = conn.cursor()

user_input = "Alice' OR '1'='1"

cur.execute(
    "SELECT * FROM students WHERE name = %s",
    (user_input,)
)

print("Safe Result:", cur.fetchall())

cur.close()
conn.close()