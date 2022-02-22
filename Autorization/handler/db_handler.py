import sqlite3

def login(login, password, signal):
    con = sqlite3.connect('C:\\Users\\vikto\\.vscode\\MyWork\\SQL_sign\\users.db')
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()
    
    if value != [] and value[0][1] == password:
        signal.emit('Успешная авторизация!')
    else:
        signal.emit('Проверьте правильность ввода данных!')

    cur.close()
    con.close()


def register(login, password, signal):
    con = sqlite3.connect('C:\\Users\\vikto\\.vscode\\MyWork\\SQL_sign\\users.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != []:
        signal.emit('Такой ник уже используется!')

    elif value == []:
        cur.execute(f"INSERT INTO users (name, password) VALUES ('{login}', '{password}')")
        signal.emit('Вы успешно зарегистрированы!')
        con.commit()

    cur.close()
    con.close()