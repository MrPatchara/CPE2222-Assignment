import tkinter as tk
import os
from tkinter import messagebox


def toggle_option_menu(shape): # ฟังก์ชันสำหรับเปิด/ปิด OptionMenu ของรูปทรง
    if shape == "Rectangle":
        if rect_var.get():
            rect_size_menu.grid(row=1, column=1, padx=5, pady=5)
            rect_color_menu.grid(row=1, column=2, padx=5, pady=5)
        else:
            rect_size_menu.grid_remove()
            rect_color_menu.grid_remove()
    elif shape == "Triangle":
        if tri_var.get():
            tri_size_menu.grid(row=2, column=1, padx=5, pady=5)
            tri_color_menu.grid(row=2, column=2, padx=5, pady=5)
        else:
            tri_size_menu.grid_remove()
            tri_color_menu.grid_remove()
    elif shape == "Circle":
        if circ_var.get():
            circ_size_menu.grid(row=3, column=1, padx=5, pady=5)
            circ_color_menu.grid(row=3, column=2, padx=5, pady=5)
        else:
            circ_size_menu.grid_remove()
            circ_color_menu.grid_remove()

def draw_shapes(): # ฟังก์ชันสำหรับวาดรูปทรง
    shapes = []
    if rect_var.get():
        shapes.append(("Rectangle", rect_size.get(), rect_color.get()))
    if tri_var.get():
        shapes.append(("Triangle", tri_size.get(), tri_color.get()))
    if circ_var.get():
        shapes.append(("Circle", circ_size.get(), circ_color.get()))

    if not shapes:
        messagebox.showwarning("Warning", "กรุณาเลือกรูปทรงที่ต้องการวาดก่อน !")
        return

    result_win = tk.Toplevel(root)
    result_win.title("RESULT")
   
    img_path = os.path.join(os.path.dirname(__file__), 'logo.png')
    img = tk.PhotoImage(file=img_path)
    result_win.tk.call('wm', 'iconphoto', result_win._w, img)

    # คำนวณขนาดของ canvas โดยพิจารณาขนาดของรูปทรงแต่ละรูป
    canvas_width = 20  # ความกว้างเริ่มต้นของ 
    canvas_height = 20  # ความสูงเริ่มต้นของ 
    shape_positions = []

    for shape, size, color in shapes: # วนลูปเพื่อคำนวณขนาดของ canvas โดยพิจารณาขนาดของรูปทรงแต่ละรูป
        if shape == "Rectangle":
            w, h = map(int, size.split("x"))
            shape_positions.append((canvas_width, 20, w, h, color, shape))
            canvas_width += w + 20  # เพิ่มความกว้างของ canvas โดยเพิ่มความกว้างของรูปทรงและระยะห่าง 20
            canvas_height = max(canvas_height, h + 40)  # 

        elif shape == "Triangle":
            w, h = map(int, size.split("x"))
            shape_positions.append((canvas_width, 20, w, h, color, shape))
            canvas_width += w + 20
            canvas_height = max(canvas_height, h + 40)

        elif shape == "Circle":
            r = int(size.split("=")[1])
            shape_positions.append((canvas_width + r, 20 + r, r, r, color, shape))
            canvas_width += 2 * r + 20
            canvas_height = max(canvas_height, 2 * r + 40)

    canvas = tk.Canvas(result_win, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack(padx=20, pady=20)

    # วนลูปเพื่อวาดรูปทรงลงบน canvas
    for x, y, w, h, color, shape_type in shape_positions:
        if color == "":
            color = "black"  # ค่าสีเริ่มต้นของรูปทรง
        if shape_type == "Rectangle":
            canvas.create_rectangle(x, y, x + w, y + h, outline="black", fill=color)
        elif shape_type == "Triangle":
            canvas.create_polygon(x, y, x + w, y, x + w, y + h, outline="black", fill=color, width=1)
        elif shape_type == "Circle":
            canvas.create_oval(x - w, y - h, x + w, y + h, outline="black", fill=color)

    close_btn = tk.Button(result_win, text="Close Window", command=result_win.destroy)
    close_btn.pack(pady=10)


# Main window
root = tk.Tk()
root.title("Canvas Drawing")
root.geometry("350x250")
root.config(padx=5, pady=5)

img_path = os.path.join(os.path.dirname(__file__), 'logo.png')
img = tk.PhotoImage(file=img_path)
root.tk.call('wm', 'iconphoto', root._w, img)

# ตัวแปรสำหรับเก็บค่าของตัวเลือกการวาดรูปทรง
rect_var = tk.BooleanVar()
tri_var = tk.BooleanVar()
circ_var = tk.BooleanVar()

rect_size = tk.StringVar(value="50x50")
tri_size = tk.StringVar(value="50x50")
circ_size = tk.StringVar(value="Radius=25")
rect_color = tk.StringVar(value="black")
tri_color = tk.StringVar(value="black")
circ_color = tk.StringVar(value="black")

# เฟรมสำหรับเก็บตัวเลือกของการวาดรูปทรง
settings_frame = tk.LabelFrame(root, text="Drawing Setting", padx=5, pady=5)
settings_frame.pack(padx=10, pady=10)

# Checkbox ของ Rectangle
rect_checkbox = tk.Checkbutton(settings_frame, text="Rectangle", variable=rect_var, command=lambda: toggle_option_menu("Rectangle"))
rect_checkbox.grid(row=1, column=0, sticky="w", padx=5, pady=5)
rect_size_menu = tk.OptionMenu(settings_frame, rect_size, "50x50", "100x50", "50x100")
rect_size_menu.grid(row=1, column=1, padx=5, pady=5)
rect_color_menu = tk.OptionMenu(settings_frame, rect_color, "black", "red", "green", "blue", "yellow")
rect_color_menu.grid(row=1, column=2, padx=5, pady=5)
rect_size_menu.grid_remove()
rect_color_menu.grid_remove()

# Checkbox ของ Triangle
tri_checkbox = tk.Checkbutton(settings_frame, text="Right Triangle", variable=tri_var, command=lambda: toggle_option_menu("Triangle"))
tri_checkbox.grid(row=2, column=0, sticky="w", padx=5, pady=5)
tri_size_menu = tk.OptionMenu(settings_frame, tri_size, "50x50", "100x50", "50x100")
tri_size_menu.grid(row=2, column=1, padx=5, pady=5)
tri_color_menu = tk.OptionMenu(settings_frame, tri_color, "black", "red", "green", "blue", "yellow")
tri_color_menu.grid(row=2, column=2, padx=5, pady=5)
tri_size_menu.grid_remove()
tri_color_menu.grid_remove()

# Checkbox ของ Circle
circ_checkbox = tk.Checkbutton(settings_frame, text="Circle", variable=circ_var, command=lambda: toggle_option_menu("Circle"))
circ_checkbox.grid(row=3, column=0, sticky="w", padx=5, pady=5)
circ_size_menu = tk.OptionMenu(settings_frame, circ_size, "Radius=25", "Radius=50", "Radius=75")
circ_size_menu.grid(row=3, column=1, padx=5, pady=5)
circ_color_menu = tk.OptionMenu(settings_frame, circ_color, "black", "red", "green", "blue", "yellow")
circ_color_menu.grid(row=3, column=2, padx=5, pady=5)
circ_size_menu.grid_remove()
circ_color_menu.grid_remove()

# Draw Button
draw_btn = tk.Button(root, text="Draw", command=draw_shapes)
draw_btn.pack(pady=10)

root.mainloop()
