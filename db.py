import sqlite3

def init_db(login:str):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f'''CREATE TABLE IF NOT EXISTS {login} (
        earning     INTEGER,
        expense     INTEGER,
        info        TEXT
    )''')
    conn.commit()

def correct(login:str, password:str):
    psw = None
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE login=?',(login, ))
    for row in c:
        psw = str(*row)
    if psw == password:
        return True
    else:
        return False

def earning(login:str, summ:int, text:str, datetime:str):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f'INSERT INTO {login} (earning, info, datetime) VALUES (?, ?, ?)', (summ, text, datetime))
    c.execute('UPDATE users SET balance=balance+? WHERE login=?', (summ, login))
    conn.commit()

def expense(login:str, summ:int, text:str, datetime:str):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f'INSERT INTO {login} (expense, info, datetime) VALUES (?, ?, ?)', (summ, text, datetime))
    c.execute('UPDATE users SET balance=balance-? WHERE login=?', (summ, login))
    conn.commit()

def get_bal(login:str):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT balance FROM users WHERE login=?', (login, ))
    for row in c:
        return str(*row)

def add_col():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('ALTER TABLE fifty59nine ADD datetime DATE')
    conn.commit()

def get_list(login:str):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM {login}')
    l = []
    f = []
    for row in c:
        for x in row:
            if x == None:
                x = 0
            f.append(x)
        l.append(f[:])
        f.clear()
    return l


if __name__ == "__main__":
    init_db('syaopin')