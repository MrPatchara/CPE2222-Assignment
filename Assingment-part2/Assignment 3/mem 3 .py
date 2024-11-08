import tkinter as tk 
import os # นำเข้าโมดูล os มาใช้งาน
from tkinter import messagebox


def toggle_option_menu(shape): # สร้างฟังก์ชัน toggle_option_menu โดยรับค่า shape
    if shape == "Rectangle": # ถ้า shape เป็น Rectangle
        if rect_var.get():
            rect_size_menu.grid(row=1, column=1, padx=5, pady=5)  # แสดง rect_size_menu ในตำแหน่งที่กำหนด
            rect_color_menu.grid(row=1, column=2, padx=5, pady=5) # แสดง rect_color_menu ในตำแหน่งที่กำหนด
        else:
            rect_size_menu.grid_remove() # ซ่อน rect_size_menu
            rect_color_menu.grid_remove() # ซ่อน rect_color_menu
    elif shape == "Triangle": # ถ้า shape เป็น Triangle
        if tri_var.get(): 
            tri_size_menu.grid(row=2, column=1, padx=5, pady=5) # แสดง tri_size_menu ในตำแหน่งที่กำหนด
            tri_color_menu.grid(row=2, column=2, padx=5, pady=5) # แสดง tri_color_menu ในตำแหน่งที่กำหนด
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

def draw_shapes():  # สร้างฟังก์ชัน draw_shapes
    shapes = []
    if rect_var.get(): # ถ้า rect_var มีค่าเป็น True
        shapes.append(("Rectangle", rect_size.get(), rect_color.get())) # เพิ่มข้อมูลเข้าไปใน shapes โดยเก็บข้อมูลของ Rectangle ที่เลือกไว้ โดยเก็บขนาดของรูปทรง และสีของรูปทรง ที่เลือกไว้  ในรูปแบบของ Tuple และเก็บไว้ใน shapes โดยใช้ append ในการเพิ่มข้อมูล  
    if tri_var.get(): # ถ้า tri_var มีค่าเป็น True
        shapes.append(("Triangle", tri_size.get(), tri_color.get())) 
    if circ_var.get(): # ถ้า circ_var มีค่าเป็น True
        shapes.append(("Circle", circ_size.get(), circ_color.get()))

    if not shapes: # ถ้าไม่มีรูปทรงที่ถูกเลือก
        messagebox.showwarning("Warning", "กรุณาเลือกรูปทรงที่ต้องการวาดก่อน !")
        return

    result_win = tk.Toplevel(root) # สร้างหน้าต่างใหม่
    result_win.title("RESULT") # ตั้งชื่อหน้าต่าง
 
    img_path = os.path.join(os.path.dirname(__file__), 'logo.png')
    img = tk.PhotoImage(file=img_path) 
    result_win.tk.call('wm', 'iconphoto', result_win._w, img) # กำหนด icon ให้กับหน้าต่างใหม่

    # Calculate the canvas size
    canvas_width = 20  
    canvas_height = 20  
    shape_positions = [] # สร้างตัวแปร shape_positions แบบ List มาเก็บข้อมูลของรูปทรงที่เลือกไว้

    for shape, size, color in shapes: # วนลูปเพื่อเรียกใช้ข้อมูลของรูปทรงที่เลือกไว้
        if shape == "Rectangle": # ถ้า shape เป็น Rectangle
            w, h = map(int, size.split("x")) # แยกขนาดของรูปทรงออกจากกัน
            shape_positions.append((canvas_width, 20, w, h, color, shape)) # เพิ่มข้อมูลของรูปทรงที่เลือกไว้ โดยเก็บข้อมูลของรูปทรง และสีของรูปทรง ที่เลือกไว้  ในรูปแบบของ Tuple และเก็บไว้ใน shape_positions โดยใช้ append ในการเพิ่มข้อมูล
            canvas_width += w + 20  # กำหนดความกว้างของ canvas
            canvas_height = max(canvas_height, h + 40)  # กำหนดความสูงของ canvas

        elif shape == "Triangle": # ถ้า shape เป็น Triangle
            w, h = map(int, size.split("x")) 
            shape_positions.append((canvas_width, 20, w, h, color, shape)) # เพิ่มข้อมูลของรูปทรงที่เลือกไว้ โดยเก็บข้อมูลของรูปทรง และสีของรูปทรง ที่เลือกไว้  ในรูปแบบของ Tuple และเก็บไว้ใน shape_positions โดยใช้ append ในการเพิ่มข้อมูล
            canvas_width += w + 20 # กำหนดความกว้างของ canvas โดยเพิ่มขนาดของรูปสามเหลี่ยม และค่าคงที่ 20
            canvas_height = max(canvas_height, h + 40)

        elif shape == "Circle": # ถ้า shape เป็น Circle
            r = int(size.split("=")[1]) #
            shape_positions.append((canvas_width + r, 20 + r, r, r, color, shape))# เพิ่มข้อมูลของรูปทรงที่เลือกไว้ โดยเก็บข้อมูลของรูปทรง และสีของรูปทรง ที่เลือกไว้  ในรูปแบบของ Tuple และเก็บไว้ใน shape_positions โดยใช้ append ในการเพิ่มข้อมูล
            canvas_width += 2 * r + 20 # กำหนดความกว้างของ canvas โดยเพิ่มขนาดของรัศมีของวงกลม และค่าคงที่ 20
            canvas_height = max(canvas_height, 2 * r + 40)

    canvas = tk.Canvas(result_win, width=canvas_width, height=canvas_height, bg="white") # สร้าง canvas โดยกำหนดความกว้างและความสูงของ canvas และกำหนดสีพื้นหลังของ canvas
    canvas.pack(padx=20, pady=20) # แสดง canvas ในตำแหน่งที่กำหนด

    # วนลูปเพื่อวาดรูปทรงที่เลือกไว้
    for x, y, w, h, color, shape_type in shape_positions: 
        if color == "": 
            color = "black"  # กำหนดสีเริ่มต้นของรูปทรงเป็นสีดำ
        if shape_type == "Rectangle":
            canvas.create_rectangle(x, y, x + w, y + h, outline="black", fill=color) # วาดรูปสี่เหลี่ยมผืนผ้า โดยกำหนดพิกัด x, y ของจุดเริ่มต้น และพิกัด x, y ของจุดสุดท้าย และกำหนดสีของรูปทรง และสีขอบของรูปทรง และความหนาของเส้นขอบ และกำหนดสีพื้นหลังของรูปทรง และความหนาของเส้นขอบ 
        elif shape_type == "Triangle": # ถ้า shape เป็น Triangle
            canvas.create_polygon(x, y, x + w, y, x + w, y + h, outline="black", fill=color, width=1) 
        elif shape_type == "Circle":
            canvas.create_oval(x - w, y - h, x + w, y + h, outline="black", fill=color) 

    close_btn = tk.Button(result_win, text="Close Window", command=result_win.destroy)
    close_btn.pack(pady=10)


# Main window
root = tk.Tk()
root.title("Canvas Drawing")
root.geometry("350x250")
root.config(padx=5, pady=5)  # กำหนดระยะขอบของโปรแกรม  5 พิกเซล ทั้งด้านซ้ายและด้านบน
# Set the window icon at the top of the program window
img_path = os.path.join(os.path.dirname(__file__), 'logo.png') # กำหนดที่อยู่ของไฟล์รูปภาพ
img = tk.PhotoImage(file=img_path)
root.tk.call('wm', 'iconphoto', root._w, img)

# ตัวแปรสำหรับเก็บค่าของรูปทรงที่เลือกไว้
rect_var = tk.BooleanVar() # สร้างตัวแปร rect_var แบบ BooleanVar
tri_var = tk.BooleanVar() # สร้างตัวแปร tri_var แบบ BooleanVar
circ_var = tk.BooleanVar() # สร้างตัวแปร circ_var แบบ BooleanVar

rect_size = tk.StringVar(value="50x50") # สร้างตัวแปร rect_size แบบ StringVar และกำหนดค่าเริ่มต้นเป็น "50x50"
tri_size = tk.StringVar(value="50x50") # สร้างตัวแปร tri_size แบบ StringVar และกำหนดค่าเริ่มต้นเป็น "50x50"
circ_size = tk.StringVar(value="Radius=25") # สร้างตัวแปร circ_size แบบ StringVar และกำหนดค่าเริ่มต้นเป็น "Radius=25"
rect_color = tk.StringVar(value="black") # สร้างตัวแปร rect_color แบบ StringVar และกำหนดค่าเริ่มต้นเป็น "black"
tri_color = tk.StringVar(value="black") # สร้างตัวแปร tri_color แบบ StringVar และกำหนดค่าเริ่มต้นเป็น "black"
circ_color = tk.StringVar(value="black") # สร้างตัวแปร circ_color แบบ StringVar และกำหนดค่าเริ่มต้นเป็น "black"

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
