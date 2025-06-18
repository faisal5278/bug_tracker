
import sqlite3


conn = sqlite3.connect('bug_tracker.db')
cursor = conn.cursor()

with open('schema.sql', 'r') as f:
    schema = f.read()
    cursor.executescript(schema)

print("Database and table created successfully!")

conn.commit()
conn.close()
