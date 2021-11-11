# Вариант 12
# Даны три целых числа: A, B, C. Проверить истинность высказывания: «Каждое из чисел A,
# B, C положительное».
A = input("Введите число А: ")
B = input("Введите число B: ")
C = input("Введите число C: ")

while type(A) != int:   # обработка исключений
    try:
        A = int(A)
    except ValueError:
        print("Неправильное число")
        A = input("Введите число А: ")
while type(B) != int:    # обработка исключений
    try:
        B = int(B)
    except ValueError:
        print("Неправильное число")
        B = input("Введите число B: ")
while type(C) != int:   # обработка исключений
    try:
        C = int(C)
    except ValueError:
        print("Неправильное число")
        C = input("Введите число С: ")

if A > 0 and B > 0 and C > 0:
    print("Все числа положительные")
else:
    print("Не все числа положительные")
