import tkinter as tk
import maze_maker
import random

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

def make_start(canvas, maze_lst): #ランダムにスタートを生成
    x, y = random.randint(0,14), random.randint(0,8)
    if maze_lst[x][y] == 0:
        canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, fill="blue")
    else:
        make_start(canvas, maze_lst)
    return x, y

def make_goal(canvas, maze_lst, sx, sy): #ランダムにゴールを生成
    x, y = random.randint(0,14), random.randint(0,8)        
    if maze_lst[x][y] == 0:
        if x == sx and y == sy:
            make_goal(canvas, maze_lst, sx, sy)
        canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, fill="red")
    else:
        make_goal(canvas, maze_lst, sx, sy)
    return x, y

def finish():
    canvas.dalete()
    goal = tk.Tk()
    goal.title("GOAL!")
    goal.geometry("750x450")
    goal.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    maze_lst = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, maze_lst)
    sx, sy = make_start(canvas, maze_lst)
    gx, gy = make_goal(canvas, maze_lst, sx, sy)
    key = ""
    mx, my = sx, sy
    cx, cy = mx*100+50, my*100+50
    image = tk.PhotoImage(file = "fig/0.png")
    canvas.pack()
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    canvas.create_image(cx, cy, image = image, tag = "kokaton")
    main_proc()
    root.mainloop()