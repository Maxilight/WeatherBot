import sqlite3
import random
live = 5
try_user = 0
comp_num = random.randint(1, 10)
print(comp_num)
while live > 0:
    try_user += 1
    user_num = int(input("Введите число: "))
    if user_num > comp_num:
        live -= 1
        print("Введенное число больше!")
        print(f'Остадлсь {live} жизней')
    if user_num < comp_num:
        live -= 1
        print("Введенное число больше!")
        print(f'Осталось {live} жизней')
    else:
        print('Вы угадали!!!')
        break

else:
    print("Вы не угадали!!!")
if live > 0:
    user_name = input('Введите ваше Имя:')
    with sqlite3.connect('game.db') as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS user_score(
        name TEXT,
        score INTEGER
        )""")
        cur.execute(f"""INSERT INTO user_score(name, score) VALUES(
        '{user_name}' {try_user}
        )""")
        con.commit()
        cur.execute("""SELECT * FROM user_score""")
        result = cur.fetchall()
        print(result)

