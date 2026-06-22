from config import get_connection

conn = get_connection()
cur = conn.cursor()

try:
    cur.execute(
        "INSERT INTO students (name, age) VALUES (%s, %s)",
        ("Bob", 22)
    )

    # Intentional error
    cur.execute("INSERT INTO invalid_table VALUES (1)")

    conn.commit()

except Exception as e:
    print("Error:", e)
    conn.rollback()

cur.execute("SELECT * FROM students")
print("After rollback:", cur.fetchall())

cur.close()
conn.close()