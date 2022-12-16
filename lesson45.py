import sqlite3

db = sqlite3.connect('db.sqlite3')
c = db.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT  NULL, 
    email TEXT NOT NULL UNIQUE, 
    password TEXT NOT NULL
)
''')

db.close()