import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("calc")
root.geometry("300x500")

button_lst = []

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo("押すな", f"{txt}のボタンがクリックされました")

for i in range(10):
    button = tk.Button(root, text = str(i),
                        font = ("", 30),
                        width = 4,
                        height = 2)
    button.bind("<1>", button_click)
    button_lst.append(button)

for i, button in enumerate(reversed(button_lst)):
    button.grid(row = int(i/3), column = i%3)

root.mainloop()