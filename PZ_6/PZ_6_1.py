#   Дан список A размера N (N — нечетное число). Вывести его элементы с нечетными
#   номерами в порядке убывания номеров: AN, AN-2, AN-4, ..., A1. Условный оператор не
#   использовать.
import random
N = int(input("Кол-во элементов массива: "))
arr = []

for i in range(N):
    ran = random.randint(1, 101)
    arr.append(ran)

print("изначальный массив - ", arr)
arr_res = arr[::-2]
for i in arr_res:
    print(i)
