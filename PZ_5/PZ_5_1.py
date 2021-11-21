#   Вариант 12
#   Составить функцию, которая выполнит суммирования числового ряда.
def sumOfRange(num):
    arr = range(1, num + 1)
    res = 0
    for i in arr:
        res += i
    print("Сумма равна = ", res)


N = int(input("Кол-во элементов: "))
sumOfRange(N)
