'''
count = 10
while count > 0:
   count -= 1
   if count == 5:
      continue
   print(count)
else:
    print('end while'
'''
#
'''
count = 10
while count > 0:
    if count % 2 == 0:
        print(count)
    count -= 1
'''
#
'''
s = input("Введите строку: ")
for i in s:

    print(f"--> {i*2} -->>")
'''
a = int(input("Введите первое число: "))
q = input("Введите действие: ")
b = int(input("Введите второе число: "))
if q == "+":
    print(a+b)
elif q == "/":
    if b != 0:
        print(a/b)
    elif b == 0:
        print("Zero")
'''
#
'''
a = input("Введите первое число: ")
    if a == "exit":
        break
    else:
        a = int(a)
    q = input("Введите действие: ")
    b = int(input("Введите второе число: "))
    if q == "+":
    print(a+b)
    elif q == "/":
    if b != 0:
        print(a/b)
    elif b == 0:
        print("Zero")
'''
#
'''
s = 'hello world'
print(s[8:10:-1])