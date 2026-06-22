from config import get_connection

conn = get_connection()
cur = conn.cursor()

# INSERT
cur.execute(
    "INSERT INTO students (name, age) VALUES (%s, %s)",
    ("Alice", 21)
)

# query = f"""
# INSERT INTO students (name, age)
# VALUES ({name}, {age});"""


# condition = "age > 18; DELETE * FROM students;"
# query = f"SELECT * FROM students WHERE {condition}"

# SELECT
cur.execute("SELECT * FROM students")
print("Students:", cur.fetchall())

# UPDATE
cur.execute(
    "UPDATE students SET age = %s WHERE name = %s",
    (25, "Alice")
)

# DELETE
# cur.execute(
#     "DELETE FROM students WHERE name = %s",
#     ("Alice",)
# )

conn.commit()

print("CRUD operations done")

cur.close()
conn.close()