def hello(name):
    return f'Привет {name}!!!! Сколько лет?' 'Какой у тебя вес?'

print(hello('Max'))
def kwfuncs(**kwargs):
    return kwargs
print(kwfuncs(a = 1, b = 22, c = 33))
def instr(a, b, *args, **kwargs):
    return args, kwargs
print(instr('Mkara', 555, [55,22,35,155], kwak = 155, man = 5))
x = 10
def showxx():
    #x = 100
    global x
    x += 10

    return x
print(x)
print(showxx())
