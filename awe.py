s = ['h', 'e', 'l', 'l', 'l', 'o']
s = ''.join(s)
print(s)
my_list = []
for i in s:
    my_list.append(i)
print(my_list)
my_list = [i for i in range(100)]
my_list_ch = []
my_list_nch = []
for i in my_list:
    if i %2 == 0:
        my_list_ch.append(i)
    else:
        my_list_nch.append(i)
print(my_list_ch)
print(my_list_nch)
s = ' Petrov Petr KB1234567890'
s = s.split()
chel = {}
chel['lastname'] = s[0]
chel['name'] = s[1]
chel['passport'] = s[2]
print(chel)
if 'name' in chel:
    print(True)
for i in chel:
    print(chel.get(i))
print(chel.get('name'))
print(chel.keys())
print(chel.values())
print(chel.items())

print(chel)
for i, j in chel.items():
    print(i,  '-->', j)
chel.setdefault('auto', 'audi')
print(chel)
chel.popitem()
print(chel)
chelik = dict.fromkeys(['a', 'b', 'c'], 'words')
print(chelik)