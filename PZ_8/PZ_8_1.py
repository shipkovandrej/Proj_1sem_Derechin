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
    print(dic.get(word))
else:
    print(getkey(dic, word))