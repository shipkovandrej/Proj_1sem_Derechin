from tkinter import *
import tkinter as tk
# Вариант 12
# Дано целое число. Вывести его строку-описание вида «отрицательное четное число»,
# «нулевое число», «положительное нечетное число» и т. д.
root = Tk()
root.title("PZ_3")
root.geometry("400x150+480+90")
root.resizable(False, False)


def close():
    root.destroy()
    root.quit()


def button_clicked(event):
    num = int(entry.get())
    print(num)
    res1 = ""  # res1 для положительное или отрицательное
    res2 = ""  # res2 для четное нечетное
    res3 = ""  # res3 для нулевого

    if num == 0:
        res3 += "нулевое"
    if num > 0:
        res1 += "положительное"
    if num < 0:
        res1 += "отрицательное"
    if num % 2 == 0 and num != 0:
        res2 += " четное"
    if num % 2 != 0 and num != 0:
        res2 += " нечетное"
    last_label['text'] = "Вы ввели " + res1 + res2 + res3 + " число"


Label(root, text="Введите целое число", font="Arial 13").pack()

entry = tk.Entry(root, font="Arial 13")
entry.pack()

button = Button(root, text='Выполнить', bg="black", fg="white", font="Arial 13", relief="flat", command="button_clicked")
button.pack()

last_label = Label(root, text='', font="Arial 13")
last_label.pack(fill=BOTH)

button.bind('<Button-1>', button_clicked)
root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()
