# Вариант 12
# В исходном текстовом файле (dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
# ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
# текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.
import re

f = open("dates.txt", 'r', encoding='utf-8')    # format1  ДД.ММ.ГГГГ   format2 ДД/ММ/ГГГГ
file = f.read()

p = re.compile(r"[0-3][0-9][.][01][0-9][.]\d{4}")
# Кол-во 1 формата
if p.findall(file):
    format1 = p.findall(file)
    format_1_len = len(format1)
    print("Кол-во записей вида ДД.ММ.ГГГГ: ", format_1_len)


# Кол-во 2 формата
p = re.compile(r"[0-3][0-9][/][01][0-9][/]\d{4}")
if p.findall(file):
    format2 = p.findall(file)
    format_2_len = len(format2)
    print("Кол-во записей вида ДД/ММ/ГГГГ: ", format_2_len)


# Новый файл под единый формат
p = re.compile(r"(\d{2}).?(\d{2}).?(\d{4})")
obrubki = ''
if p.findall(file):
    obrubki = p.findall(file)
f1 = open("test1.txt", "w", encoding="utf-8")

for i in range(len(obrubki)):
    f1.write("/".join(obrubki[i]) + "\n")

f.close()
f1.close()
