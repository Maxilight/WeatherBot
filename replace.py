'''
string = input('Строка: ')
sim = input('Символ: ')
new_str = ' '
for i in string:
    if i == sim:
        new_str += ' '
    else:
        new_str += i
print(new_str)
'''
#
string = input('Строка: ')
sim = input('Символ: ')
new_str = string.replace(sim, ' ')
print(new_str)