#   Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
#   списка вправо на K позиций (при этом A1 перейдет в AK+1, A2 — в AK+2, ..AN-K — в AN, а
#   исходное значение K последних элементов будет потеряно). Первые K элементов
#   полученного списка положить равными 0.
import random

N = int(input("Кол-во элементов маcсива: "))
k = int(input("Сдвиг на кол-во позиций: "))
arr = []

for i in range(N):
    arr.append(random.randint(1, 11))

print(arr)  # Вывод массива с которым будем работать

for i in range(N - 1, -1, -1):  # перебираем список в обратном порядке и по форуле ставим значения
    if i >= k:
        arr[i] = arr[i-k]
    elif i < k:
        arr[i] = 0
print(arr)
