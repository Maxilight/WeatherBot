'''
s = 'hello world'

print(s[::-4])
print(len(s))
print(s.capitalize())
print(s.count('e', 5, 11))
n = '500'
print(n.ljust(5, '0'))
print(s.replace('l', '%'))
'''
#
'''
l = ''
for i in s:
    if i == 'l':
        l += i
print(l)
q = input("Введите строку: ")
if q == q[::-1]:
    print("polindrom!")
'''
#
'''
from time import sleep as spi
for i in range(20):
    print(i)
    spi(2)
'''
#
'''
from random import randint, choice, random
s = 'hello world'
print(choice(s))
q = 123456
print (randint(1, 10))
'''
#
'''
#for countdown in 5, 4, 3, 2, 1, 'hey!':
    #print(countdown)
cliches = [
 "At the end of the day",
 "Having said that",
 "The fact of the matter is",
 "Be that as it may",
 "The bottom line is",
 "If you will",
 ]
print(cliches[3])
quotes = {
 "Moe": "A wise guy, huh?",
 "Larry": "Ow!",
 "Curly": "Nyuk nyuk!",
 }
stooge = "Curly"
print(stooge, "says:", quotes[stooge])
'''
a = input("Введите что-то: ")
if a == (""):
    print("")
else:
    print("OK")
'''
#
'''
opros = int(input("Введите число: "))
if opros > 0:
    print(1)
else:
    opros < 0
    print(-1)
'''
#
'''
string = input("Введите строку: ")
sim = input("Введите символ: ")
new_stri = ""
for i in string:
    if i == sim:
        new_stri += ' '
    else:
        new_stri += i
print(new_stri)
'''
#
'''
string = input("Введите строку: ")
sim = input("Введите символ: ")
new_stri = string.replace(sim, ' ')
print(new_stri)
'''
#

import random
'''
print("Компьютер загадал число, вам нужно его угадать.")
start = int(input("Начало диапазона: "))
stop = int(input("Конец диапазона: "))
comp_number = random.randint(start, stop)
live = 5
while live > 0:
    print(comp_number)
    print(f"Кол-во попыток: {live}")
    user_number = int(input("Введите число: "))
    if comp_number > user_number:
        print("Загаданное число больше!")
        live -= 1
    elif user_number > comp_number:
        print("Загаданное число меньше!")
        live =- 1
    else:
        comp_number == user_number
        print("Вы угадали!")
        break
else:
    print("Вы проиграли!")
'''
#
'''
al = "qwertyuiop"
new_str = ''
for i in range(5):
    new_str += random.choice(al)
print(new_str)
'''
#
'''
al = "qwerwetgjtyuiop"
new_str1 = ''
new_str2 = ''
for i in range(random.randint(2, 5)):
    new_str1 += random.choice(al)
for i in range(random.randint(2, 5)):
    new_str2 += random.choice(al)
new_str3 = new_str1 + ' ' + new_str2
print(new_str3)
'''
#
'''
live = 3
while live > 0:
    p = 'PasSword777'
    u_p = input("Введите пароль: ")
    if p.upper() == u_p.upper():
        print('Добро пожаловать!')
    else:
        print("Вход запрещен!")
        live -= 1
else:
    print("@@@")
'''
#


'''
s = 'hello world'
col = len(s)
print(col)
index = 0
while col > 0:
    print(s[index])
    index =+ 1
    col -= 1
'''
#
'''
s = 'hello wolrd'
m_l = []
for i in s:
    m_l.append(i)
print(i)

