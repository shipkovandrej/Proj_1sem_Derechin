#   Вариант 12
#   Дано целое число N (>1). Вывести наибольшее из целых чисел K, для которых сумма 1 + 2
# + ... + K будет меньше или равна N, и саму эту сумму.

def kcheck(k):
    res = 0
    while k > 0:
        res += k    # через функцию нельзя, хотя через нее намного короче
        k -= 1
    return res

N = input("Число N: ")

while type(N) != int:   # обработка исключений
    try:
        N = int(N)
    except ValueError:
        print("Неправильное число")
        N = int(input("Введите целое число: "))

K = N
flag = 0
num = "ошибка"
while K > 0:
    if flag == 0:
        res = 0
        i = K
        while i > 0:
            res += i
            i -= 1
        if res <= N:
            num = K
            flag = 1
            print("Сумма = ", res)
            break
        K -= 1
    else:
        break
print("число К = ", num)

