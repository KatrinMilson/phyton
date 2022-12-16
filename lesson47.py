import sqlite3

db = sqlite3.connect('db.sqlite3')
c = db.cursor()
email = "petrov@gmail.com"
c.execute('SELECT * FROM users WHERE email = ? OR name = ?', (email, 'John Doe'))
# res = c.fetchone()

c.execute('SELECT * FROM users')
res = c.fetchall()
for i in res:
    print(i[1], i[2])

print(res)
db.close()
