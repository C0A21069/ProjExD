import tkinter as tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    x, y = mx, my
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_lst[mx][my] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        mx, my = x, y
    canvas.coords("kokaton", cx, cy)
    root.after(125, main_proc)

if __name__ == "__main__":
    key = ""
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    image = tk.PhotoImage(file = "fig/0.png")
    canvas.pack()
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    maze_lst = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, maze_lst)
    canvas.create_image(cx, cy, image = image, tag = "kokaton")
    main_proc()
    root.mainloop()