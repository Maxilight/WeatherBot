def my_len(ittera):
    count = 0
    for i in ittera:
        count += 1
    return count
print(len('hello wolrd'))
print(my_len('hello wolrd'))

def my_max(*args):
    min = 0
    for i in args:
        if i < min:
            min = i
    return min
print(min(1, 5, 155, 25, 32))
print(my_max(1, 2, 4, 55, 14))

def allsum(*args):
    sum = 0
    for i in args:
        sum + 1
    return sum
print(allsum(1, 2, 3))
