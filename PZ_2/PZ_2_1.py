# Вариант 12
# Дано двузначное число. Найти сумму и произведение его цифр.
a = True
while a:    # используем цикл while
    num = input("Введите двухзначное число: ")
    if type(num) != int:    # обработка исключения на челое число
        try:
            num = int(num)
        except ValueError:
            print("Неправильное число")
            break
    if 9 < num < 100:   # проверка на диапазон
        pass
    else:
        print("неправильное число")
        break
    num_arr = list(str(num))    # тип данных str переводим в массив
    num1 = int(num_arr[0])
    num2 = int(num_arr[1])  # выполняем матиематическе операции с первой и второй цифрой
    multi = num1 * num2
    sum = num1 + num2
    result = "умножение = " + str(multi) + "  сложение = " + str(sum)
    print(result)
    a = False   # предотвращаем бесконечный цикл
