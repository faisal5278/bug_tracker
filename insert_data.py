
import sqlite3
import json

conn = sqlite3.connect('bug_tracker.db')
cursor = conn.cursor()


with open('sample_bugs.json', 'r') as f:
    bugs = json.load(f)


for bug in bugs:
    cursor.execute('''
        INSERT INTO bugs (title, description, severity, status, module, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        bug['title'],
        bug['description'],
        bug['severity'],
        bug['status'],
        bug['module'],
        bug['created_at']
    ))

print("Bug data inserted successfully!")

conn.commit()
conn.close()
