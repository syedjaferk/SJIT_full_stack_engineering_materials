from config import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
""")

conn.commit()

print("Table created successfully")

cur.close()
conn.close()