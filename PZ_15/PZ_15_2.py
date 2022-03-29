# Вариант 12
# В матрице найти минимальный элемент в предпоследней строке.
import random

columns = 6
rows = 5

print("Матрица имеет вид:")
matrix = [[random.randint(1, 10) for x in range(columns)] for y in range(rows)]
for i in matrix:
    print(i)

my_row = len(matrix) - 2


print("Минимальный элемент в предпоследней строке", min(matrix[my_row]))
