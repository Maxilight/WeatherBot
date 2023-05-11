my_dict = {'a': 1, 'b': 2, 'c': 3}
my_list = [22, 33, 44]
new_dict = {}
new_key = []
new_value = []
for i in my_dict:
    new_key.append(i)

for i in my_dict.values():
    new_value.append(i)

count = -1
for i in my_dict:
    count += 1
    new_dict[my_list[count]] = new_value[count]

print(new_dict)
