'''
my_dict = {}
while True:
    my_key = input("Введите ключ: ")
    if my_key == "exit":
        break
    my_value = input("Введите значение: ")
    my_dict[my_key] = my_value
#print(my_dict)
choice = input("Оставить ключ как есть или ввести новый? y/n:")
if choice == 'n':
    print(my_dict)
elif choice == 'y':
    new_key = input("Введите новый ключ: ")
    new_value = input("Введите новое значение: ")
    my_dict[new_key] = new_value
print(my_dict)
'''
#
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_list = [22, 33, 44]
count = -1
for key, value in my_dict.items():
    count += 1
    my_dict[key] = my_list[count]
print(my_dict)

