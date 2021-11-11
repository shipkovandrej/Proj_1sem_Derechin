# Вариант 12
# Дано целое число N (&gt;0). Найти значение выражения 1.1 - 1.2 + 1.3 - ... (N слагаемых, знаки
# чередуются). Условный оператор не использовать.
import math
N = input("количество слагаемых: ")
while type(N) != int:   # обработка исключений
    try:
        N = int(N)

    except ValueError:
        print("Неправильное число")
        N = int(input("Введите целое число: 1"))
try:
    while N < 0 or type(N) != int:
        print("Неправильное число")
        N = input("Введите целое число: 2")
        break
except TypeError:
    print("Неправильное число")
    N = input("Введите целое число: 3")

while type(N) != int:   # обработка исключений
    try:
        N = int(N)

    except ValueError:
        print("Неправильное число")
        N = int(input("Введите целое число: 4"))

firstNum = 1.1
firstNum *= (-1) ** int(N)
res = 0
while N > 0:
    print("число ", round(firstNum, 1), "N = ", N)
    res += round(firstNum, 1)
    N -= 1
    firstNum = math.fabs(firstNum) + 0.1    # модуль числа для коректного сложения
    firstNum *= (-1) ** N
print("сумма =  ", round(res, 1))
