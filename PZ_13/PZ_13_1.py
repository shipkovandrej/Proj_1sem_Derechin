#   Вариант 12
import random
N = int(input("Число случайных символов: "))

arr1 = [random.randint(-10, 10) for x in range(N)]
arr2 = [n for n in arr1 if n > 0]

print("Исходная последовательность", arr1)
print("Конечная последовательность", arr2)
print("Кол-во положительных чисел", len(arr2))
