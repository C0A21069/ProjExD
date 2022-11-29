import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("calc")
root.geometry("300x500")

button_lst = []

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=":
        ans = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, ans)
    else:
        entry.insert(tk.END, txt)

entry = tk.Entry(root, width = 10, 
                justify = "right", 
                font = ("", 40))
entry.grid(row = 0, column= 0, columnspan = 3)

for i in range(9, -1, -1):
    button = tk.Button(root, text = str(i),
                        font = ("", 30),
                        width = 4,
                        height = 2)
    button.bind("<1>", button_click)
    button_lst.append(button)

operators =["+", "="]
for i in operators:
    button = tk.Button(root, text = i,
                        font = ("", 30),
                        width = 4,
                        height = 2)
    button.bind("<1>", button_click)
    button_lst.append(button)

for i, button in enumerate(button_lst):
    button.grid(row = int(i/3)+1, column = i%3)

root.mainloop()