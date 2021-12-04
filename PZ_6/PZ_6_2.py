#   Дан список размера N. Найти два соседних элемента, сумма которых максимальна, и
#   вывести эти элементы в порядке возрастания их индексов.
import random

N = int(input("кол-во элементов: "))

arr = []
for i in range(N):
    ran = random.randint(1, 11)  # создание массива размером N
    arr.append(ran)

x1, x2 = arr[0], arr[1]
max = x1 + x2

for i in range(1, len(arr) - 1):  # Находим максимальное значение 2 раядом стоящих чисел
    s = arr[i] + arr[i + 1]
    if s > max:
        max = s
        x1, x2 = arr[i], arr[i + 1]

print(arr)
print(x1, x2)
