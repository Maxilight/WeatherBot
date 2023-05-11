import sqlite3
name1 = input("Введите ваше имя: ")
age1 = input("Введите ваш возраст: ")
with sqlite3.connect('newbaza.db') as con:
    cur = con.cursor()


    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    old INTEGER
    )""")
    cur.execute(f"""INSERT INTO users(name, old) VALUES('{name1}', {age1})""")
    cur.execute("""SELECT * FROM users""")
    result = cur.fetchall()
    con.commit()
    print(result)
