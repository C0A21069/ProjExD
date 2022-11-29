import tkinter as tk
import tkinter.messagebox as tkm
import re

root = tk.Tk()
root.title("calc")

wid = 4
hei = 2
count = 0
button_lst = []
button_ope = []

def button_click(event): #ボタンを押したら
    global count
    btn = event.widget
    txt = btn["text"]
    siki = entry.get()
    if txt == "=":
        equrl_click(siki)
    elif txt in operators:
        operator_click(siki, txt)
    elif txt == ".":
        point_click(siki, txt)
    elif txt == "c": #リセット
        entry.delete(0, tk.END)
        count = 0
    elif siki == "0": #先頭の0禁止
        entry.delete(-1)
    else:
        entry.insert(tk.END, txt)

def equrl_click(siki): #＝を押したら
    global count
    if "×" or "÷" in siki:
            siki = re.sub("×", "*", siki)
            siki = re.sub("÷", "/", siki)
    ans = eval(siki)
    if "." in str(ans):
        count = 1
    count = 0
    entry.delete(0, tk.END)
    entry.insert(tk.END, ans)

def operator_click(siki, txt): #演算子を押したら
    global count
    if siki[-1] in operators:
        pass
    elif siki[-1] == ".":
        pass
    else:
        count += 1
        entry.insert(tk.END, txt)

def point_click(siki, txt): #小数点を押したら
    if siki[-1] in operators:
        pass
    elif siki[-1] == ".":
        pass
    elif count < siki.count("."):
        pass
    else:
        entry.insert(tk.END, txt)  

entry = tk.Entry(root, width = 14, 
                justify = "right", 
                font = ("", 40))
entry.grid(row = 0, column = 0, columnspan = 5)

for i in range(9, -1, -1):
    button = tk.Button(root, text = str(i),
                        font = ("", 30),
                        width = wid,
                        height = hei)
    button.bind("<1>", button_click)
    button_lst.append(button)

button = tk.Button(root, text = ".",
                        font = ("", 30),
                        width = wid,
                        height = hei)
button.bind("<1>", button_click)
button_lst.append(button)

operators =["÷", "×", "-", "+", "="]
for i in operators:
    button = tk.Button(root, text = i,
                        font = ("", 30),
                        width = wid,
                        height = hei)
    button.bind("<1>", button_click)
    button_ope.append(button)

button = tk.Button(root, text = "c",
                        font = ("", 30),
                        width = wid,
                        height = hei)
button.bind("<1>", button_click)
button.grid(row = 1, column = 0)

for i, button in enumerate(button_lst):
    if button["text"] == "0":
        button.grid(row = int(i/3)+2, column = i%3)
    else:
        button.grid(row = int(i/3)+2, column = 2-i%3)

for i, button in enumerate(button_ope):
    button.grid(row = i+1, column = 4)

root.mainloop()