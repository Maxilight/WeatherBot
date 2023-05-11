from    random  import randint

N=5 # Количество цифр для сравнения

nums = [randint(1, 20) for i in range(N)]

print (nums)

myMax = nums[0]
myMin = nums[0]

for i in range(N):
    if nums[i] > myMax : myMax=nums[i]
    if nums[i] < myMin : myMin=nums[i]

print ('Max:', myMax, 'Min:', myMin)