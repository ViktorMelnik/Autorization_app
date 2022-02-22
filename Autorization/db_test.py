import sqlite3

base = sqlite3.connect('users.db')
cur = base.cursor()
base.execute('CREATE TABLE IF NOT EXISTS {}(login, password)'.format('users'))
base.commit()
cur.execute('INSERT INTO users VALUES(?, ?)', ('viktor', '123456'))
base.commit()
