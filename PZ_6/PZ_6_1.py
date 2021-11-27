import random
N = 7
arr = []
for i in range(N):
    ran = random.randint(1, 101)
    arr.append(ran)
num = 0
print(arr)
for i in range(7):
    num1 = (N - 1) - num
    print(arr[num1])
    num += 2
