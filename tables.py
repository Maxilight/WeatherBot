import sqlite3

#con = sqlite3.connect('baza.db')
#cur = con.cursor()
#cur.execute("""""")
#con.close()

with sqlite3.connect('C:/Users/user/baza') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    old INTEGER,
    score INTEGER
    )""")

    cur.execute("""INSERT INTO users VALUES("Masha", 20, 1500)""")
    cur.execute("""INSERT INTO users(name, old) VALUES("Fedor", 30)""")
    cur.execute("""INSERT INTO users VALUES("Ivan", 33, 2000)""")
    cur.execute("""SELECT * FROM users""")
    result = cur.fetchall()
    print(result)
    cur.execute("""DELETE FROM users WHERE name == 'Masha' """)
    cur.execute("""SELECT * FROM users""")
    result = cur.fetchall()
    print(result)
    cur.execute("""UPDATE users SET score = 2000 WHERE name == 'Fedor' """)
    cur.execute("""SELECT * FROM users""")
    result = cur.fetchall()
    print(result)
    con.commit()