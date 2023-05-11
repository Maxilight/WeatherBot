'''
def hello_decor(fu):
    def wrapper():
        print('Hello1')
        fu()
        print('Hello2')
    return wrapper()
def func():
    print('Hello wolrd!')
per = hello_decor(func)
func()
'''
def decorator_func(func):
    def wrapper():
        print('Функция обертка')
        func()
        print('Конец функции обертки ')
    return wrapper()
@decorator_func
def hello_world():
    print('Hello world')
hello_world
@decorator_func
def goodbyeworld():
    print('Goodbye world')

