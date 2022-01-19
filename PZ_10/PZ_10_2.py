# Вариант 12
file1 = open('test.txt', 'r', encoding="UTF-8")
text = file1.read()
arr = list(text)
count = 0

for i in arr:
    if i == " ":
        count += 1

print("\n")
print("Количсество пробелов = ", count)

file1.close()
file1 = open('test.txt', 'r', encoding="UTF-8")
file2 = open("text.txt", 'w', encoding="UTF-8")
numOfStars = 10
while True:
    row = file1.readline()
    if not row:
        break
    file2.write(row)
    file2.write("*" * numOfStars)

    file2.write("\n")

file1.close()
file2.close()
