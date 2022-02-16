from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox

root = Tk()
root.title("new acc")
root.geometry("957x800+480+90")
root.resizable(False, False)


def close():
    root.destroy()
    root.quit()


font = "Calibri 17"
Label(root, text="Create an account", font="Arial 22 bold").place(x=55, y=20)
Label(root, text="Please complete all fields", font="Arial 13").place(x=55, y=66)

# 1 колонка
Label(root, text="First Name", font="Arial 11").place(x=55, y=140)
entry = tk.Entry(root, font=font, relief="flat")
entry.place(x=57, y=165, width=399, height=43)

Label(root, text="Job Title", font="Arial 11").place(x=55, y=233)
entry = tk.Entry(root, font=font, relief="flat")
entry.place(x=57, y=258, width=399, height=43)

Label(root, text="Password", font="Arial 11").place(x=55, y=326)
entry = tk.Entry(root, font=font, relief="flat")
entry.place(x=57, y=351, width=399, height=43)

Label(root, text="Phone", font="Arial 11").place(x=55, y=419)
entry = tk.Entry(root, font=font, relief="flat")
entry.place(x=57, y=444, width=399, height=43)

Label(root, text="Employees", font="Arial 11").place(x=55, y=512)

combo = Combobox(root, font="Arial 17")
combo['values'] = ('Работник1', 'Работник2', 'Работник3', 'Работник4')
combo.current()
combo.place(x=57, y=537, width=400, height=45)

# 2 колонка
Label(root, text="Last Name", font="Arial 11").place(x=503, y=140)
entry = tk.Entry(root, font=font, relief="flat")
entry.place(x=505, y=165, width=399, height=43)

Label(root, text="Email", font="Arial 11").place(x=503, y=233)
entry = tk.Entry(root, font=font, relief="flat")
entry.place(x=505, y=258, width=399, height=43)

Label(root, text="Re-enter Password", font="Arial 11").place(x=503, y=326)
entry = tk.Entry(root, font=font, relief="flat")
entry.place(x=505, y=351, width=399, height=43)

Label(root, text="Company", font="Arial 11").place(x=503, y=419)
entry = tk.Entry(root, font=font, relief="flat")
entry.place(x=505, y=444, width=399, height=43)

Label(root, text="Country", font="Arial 11").place(x=503, y=512)
combo = Combobox(root, font="Arial 17")
combo['values'] = ('Россия', 'Казахстан', 'Беларусь', 'Украина')
combo.current()
combo.place(x=505, y=537, width=400, height=45)

# 2 галочки и кнопка

text1 = "I give consent to receiving text messages (carrier charges may apply)"
text2 = "I accept the Terms of Use"
Checkbutton(root, text=text1, font="Arial 11", fg="#8f8f8f").place(x=57, y=620)
Checkbutton(root, text=text2, font="Arial 11", fg="#8f8f8f").place(x=57, y=665)

Button(root, text='Sign up', bg="#327ed0", fg="white", font="Arial 13", width=43, height=2, relief="flat").place(x=57, y=700)
root.mainloop()
