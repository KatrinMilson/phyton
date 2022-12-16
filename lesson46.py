import sqlite3

db = sqlite3.connect('db.sqlite3')
c = db.cursor()

# c.execute('INSERT INTO users (name, email) VALUES ("Иванов Иван", "ivan@gmail.com")')
# c.execute('INSERT INTO users (name, email) VALUES ("Петров Петр", "petrov@gmail.com")')
# c.execute('INSERT INTO users (name, email) VALUES ("Сидоров Сидр", "sidorov@gmail.com")')

# c.executescript('''
# INSERT INTO users (name, email) VALUES ("Jonh Doe", "doe@gmail.com");
# INSERT INTO users (name, email) VALUES ("Nick Sand", "sand@gmail.com");
# ''')

# users = [
#     ('User1', 'user1@gmail.ru'),
#     ('User2', 'user2.com'),
# ]
#
# c.executemany('INSERT INTO users (name, email, password) VALUES (?, ?)', users)

db.commit()
db.close()
