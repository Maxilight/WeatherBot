#my_dict = {'a': 1, 'b': 2, 'c': 3}
#my_key = input("Введите ключи: ")
#if my_key in my_dict:
 #   print(True)
#else:
 #   my_dict.setdefault(my_key, None)
#print(my_dict)
'''
a = 10
b = 0
try:
    c = a//b
except ZeroDivisionError:
    c = 'ZeroDivisionError'
except TypeError:
    c = 'lol'
else:
    print('all okay')
finally:
    print('Всегда отработает')
print(c)
print('finish')

d = 10
try:
    d = str(d)
except BaseException:
    print(d)

name = 'Victor'
if name == 'Victor':
    raise KeyboardInterrupt
print('finish')
'''
#
'''
m_list = [55, 22, 77, 5, 33, 122]
m_max = 0
for i in m_list:
    if m_max < i:
        m_max = i
m_min = m_max
for i in m_list:
    if m_min > i:
        m_min = i
print(m_max, m_min)
'''
s = 'Hello wolrD'
al = 'qwertyuiopzxcvbnm'
Al = 'QWERTYUIOPZXCVBNM'
new_s = ''
s = list[s]
for i in s:
    if i in al:
        new_s += al[0] == Al[0]
    print(new_s)



