# Вариант 12
# Организовать словарь на 10 англо-русских слов, обеспечивающий
# "перевод" английского слова на русский.
def getkey(dic, target):
    for key, value in dic.items():
        if value == target:
            return key

dic = {"стол": "table",
       "птица": "bird",
       "слон": "elephant",
       "собака": "dog",
       "кошка": "cat",
       "мышь": "mouse",
       "машина": "car",
       "дом": "house", }

word = input("Слово: ")
if dic.get(word):
    print("Перевод слова:", dic.get(word))
else:
    print("Перевод слова:", getkey(dic, word))
