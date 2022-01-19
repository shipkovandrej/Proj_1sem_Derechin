#  Вариант 12
list = ['-99 6 12 -36 20 45 100 -15 -10']
file1 = open('test1.txt', 'w', encoding='UTF-8')
file1.writelines(list)
file1.close()

file3 = open("test1.txt")
row = file3.read()
file3.close()
arr = row.split()
for i in range(len(arr)):
    arr[i] = int(arr[i])

NumOfElems = len(arr)
MaxElem = max(arr)
firstThird = len(arr) // 3
sum = 0
count = 0
for i in range(firstThird):
    sum += arr[i]
    count += 1
avg = sum / count
if sum % count == 0:
    avg = round(avg)
else:
    avg = round(avg, 1)

with open('test2.txt', 'w', encoding="UTF-8") as f:
    f.write("Исходные данные: ")
    f.writelines(list)
    f.write("\n")

    f.write("Количсество элементов: ")
    f.writelines(str(NumOfElems))
    f.write("\n")

    f.write("Максимальный элемент: ")
    f.writelines(str(MaxElem))
    f.write("\n")

    f.write("Среденее арифметическое первой трети: ")
    f.writelines(str(avg))
