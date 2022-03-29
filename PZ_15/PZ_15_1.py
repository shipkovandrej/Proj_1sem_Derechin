#Вариант 12
# В матрице найти сумму и произведение элементов столбца N (N задать с
# клавиатуры).
import random

columns = 3
rows = 3

print("Матрица имеет вид:")
matrix = [[random.randint(1,10) for x in range(rows)] for y in range(columns)]
for i in matrix:
    print(i)

N = int(input("Выберите столбец от 1 до 3: "))
sum = 0
multi = 1
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        #print(matrix[i][j], "  i=", i, "    j=", j)
        if j == N - 1:
            sum += matrix[i][j]
            multi *= matrix[i][j]
            break

print("Cумма : ", sum)
print("Умножеине : ", multi)