# โปรแกรมสำหรับวาดรูปทรงต่างๆ โดยผู้ใช้สามารถเลือกวาดรูปทรงได้หลายรูปพร้อมกัน
import tkinter as tk  # นำเข้าโมดูล tkinter เพื่อสร้าง GUI
from tkinter import messagebox  # นำเข้า messagebox เพื่อแสดงกล่องข้อความเตือน

# ฟังก์ชันสำหรับแสดงหรือซ่อนเมนูตัวเลือกขนาดของรูปทรงตามที่ผู้ใช้เลือก
def toggle_option_menu(shape):
    # สร้าง dictionary เก็บอ้างอิงเมนูตัวเลือกขนาดสำหรับแต่ละรูปทรง
    option_menus = {
        "Rectangle": rect_size_menu,
        "Triangle": tri_size_menu,
        "Circle": circ_size_menu
    }
    # ตรวจสอบว่าเลือก "Rectangle" และตัวแปร rect_var มีค่า True
    if shape == "Rectangle" and rect_var.get():
        option_menus[shape].grid(row=1, column=1, padx=5, pady=5)  # แสดงเมนูขนาดของสี่เหลี่ยม
    # ตรวจสอบว่าเลือก "Triangle" และตัวแปร tri_var มีค่า True
    elif shape == "Triangle" and tri_var.get():
        option_menus[shape].grid(row=2, column=1, padx=5, pady=5)  # แสดงเมนูขนาดของสามเหลี่ยม
    # ตรวจสอบว่าเลือก "Circle" และตัวแปร circ_var มีค่า True
    elif shape == "Circle" and circ_var.get():
        option_menus[shape].grid(row=3, column=1, padx=5, pady=5)  # แสดงเมนูขนาดของวงกลม
    else:
        option_menus[shape].grid_remove()  # ซ่อนเมนูขนาดหากไม่เลือกหรือเปลี่ยนการเลือก

# ฟังก์ชันสำหรับวาดรูปทรงต่างๆ ลงในหน้าต่างใหม่
def draw_shapes():
    # สร้างรายการของข้อมูลรูปทรงที่จะวาดโดยเช็คว่ารูปทรงถูกเลือกหรือไม่
    shapes = [
        ("Rectangle", rect_size.get(), "red") if rect_var.get() else None,  # เพิ่มข้อมูลสี่เหลี่ยมถ้าเลือก
        ("Triangle", tri_size.get(), "green") if tri_var.get() else None,  # เพิ่มข้อมูลสามเหลี่ยมถ้าเลือก
        ("Circle", circ_size.get(), "blue") if circ_var.get() else None  # เพิ่มข้อมูลวงกลมถ้าเลือก
    ]
    shapes = [shape for shape in shapes if shape]  # ลบค่า None ออกจากรายการ (ถ้าไม่มีการเลือก)

    # ตรวจสอบว่ารายการ shapes ว่างเปล่าหรือไม่ (กรณีที่ไม่ได้เลือกอะไร)
    if not shapes:
        messagebox.showwarning("Warning", "กรุณาเลือกรูปทรงที่ต้องการวาดก่อน!")  # แสดงข้อความเตือน
        return  # ออกจากฟังก์ชัน

    # สร้างหน้าต่างใหม่เพื่อแสดงผลลัพธ์การวาดรูปทรง
    result_win = tk.Toplevel(root)
    result_win.title("RESULT")  # ตั้งชื่อหน้าต่างผลลัพธ์

    canvas_width = canvas_height = 20  # กำหนดค่าเริ่มต้นของความกว้างและความสูงของ canvas
    shape_positions = []  # สร้างรายการสำหรับเก็บข้อมูลตำแหน่งและขนาดของรูปทรง

    # วน loop ผ่านข้อมูลใน shapes เพื่อกำหนดขนาดและตำแหน่งของแต่ละรูปทรง
    for shape, size, color in shapes:
        if shape == "Rectangle":
            w, h = map(int, size.split("x"))  # แปลงขนาดเป็นจำนวนเต็มสำหรับสี่เหลี่ยม
        elif shape == "Triangle":
            w, h = map(int, size.split("x"))  # แปลงขนาดเป็นจำนวนเต็มสำหรับสามเหลี่ยม
        elif shape == "Circle":
            r = int(size.split("=")[1])  # ดึงรัศมีจาก string ที่แสดงขนาดของวงกลม
            w = h = 2 * r  # คำนวณเส้นผ่านศูนย์กลาง
        # เพิ่มข้อมูลตำแหน่งของรูปทรงในรายการ shape_positions
        shape_positions.append((canvas_width, 20, w, h, color, shape))
        canvas_width += (w + 20)  # เพิ่มค่าความกว้างของ canvas เพื่อให้เว้นระยะห่าง
        canvas_height = max(canvas_height, h + 40)  # ปรับค่าความสูงตามขนาดของรูปทรงที่ใหญ่ที่สุด

    # จำกัดขนาดความกว้างและความสูงของ canvas ไม่ให้เกินขนาดที่กำหนด
    canvas_width = min(canvas_width, 600)
    canvas_height = min(canvas_height, 400)

    # สร้าง canvas เพื่อแสดงรูปทรงที่ถูกเลือก
    canvas = tk.Canvas(result_win, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack(padx=20, pady=20)  # จัดวาง canvas พร้อมระยะห่าง

    # วน loop ผ่านข้อมูลใน shape_positions เพื่อวาดรูปทรงลงใน canvas
    for x, y, w, h, color, shape_type in shape_positions:
        if shape_type == "Rectangle":
            canvas.create_rectangle(x, y, x + w, y + h, outline="black", fill=color)  # วาดสี่เหลี่ยม
        elif shape_type == "Triangle":
            canvas.create_polygon(x, y, x + w, y, x + w, y + h, outline="black", fill=color)  # วาดสามเหลี่ยม
        elif shape_type == "Circle":
            canvas.create_oval(x, y, x + w, y + h, outline="black", fill=color)  # วาดวงกลม

    # สร้างปุ่มปิดหน้าต่างผลลัพธ์
    tk.Button(result_win, text="Close Window", command=result_win.destroy).pack(pady=10)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Canvas Drawing")  # ตั้งชื่อหน้าต่างหลัก
root.geometry("270x220")  # กำหนดขนาดหน้าต่างหลัก
root.config(padx=5, pady=5)  # กำหนดระยะห่างภายในหน้าต่างหลัก

# กำหนดตัวแปร BooleanVar เพื่อใช้กับ checkbox แต่ละตัวสำหรับการเลือกชนิดของรูปทรง
rect_var, tri_var, circ_var = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()

# กำหนดตัวแปร StringVar เพื่อเก็บขนาดของรูปทรงที่เลือก
rect_size, tri_size, circ_size = tk.StringVar(value="50x50"), tk.StringVar(value="50x50"), tk.StringVar(value="Radius=25")

# สร้างเฟรมสำหรับการตั้งค่า (Drawing Setting)
settings_frame = tk.LabelFrame(root, text="Drawing Setting", padx=5, pady=5)
settings_frame.pack(padx=10, pady=10)  # จัดวางเฟรมพร้อมระยะห่างภายนอก

# สร้าง checkbox สำหรับเลือกวาดสี่เหลี่ยม พร้อมเชื่อมกับฟังก์ชัน toggle_option_menu
rect_checkbox = tk.Checkbutton(settings_frame, text="Rectangle", variable=rect_var, command=lambda: toggle_option_menu("Rectangle"))
rect_checkbox.grid(row=1, column=0, sticky="w", padx=5, pady=5)  # จัดวาง checkbox
# สร้างเมนูเลือกขนาดสำหรับสี่เหลี่ยมและซ่อนเมนูเริ่มต้น
rect_size_menu = tk.OptionMenu(settings_frame, rect_size, "50x50", "100x50", "50x100")
rect_size_menu.grid(row=1, column=1, padx=5, pady=5)
rect_size_menu.grid_remove()

# สร้าง checkbox สำหรับเลือกวาดสามเหลี่ยม พร้อมเชื่อมกับฟังก์ชัน toggle_option_menu
tri_checkbox = tk.Checkbutton(settings_frame, text="Right Triangle", variable=tri_var, command=lambda: toggle_option_menu("Triangle"))
tri_checkbox.grid(row=2, column=0, sticky="w", padx=5, pady=5)
# สร้างเมนูเลือกขนาดสำหรับสามเหลี่ยมและซ่อนเมนูเริ่มต้น
tri_size_menu = tk.OptionMenu(settings_frame, tri_size, "50x50", "100x50", "50x100")
tri_size_menu.grid(row=2, column=1, padx=5, pady=5)
tri_size_menu.grid_remove()

# สร้าง checkbox สำหรับเลือกวาดวงกลม พร้อมเชื่อมกับฟังก์ชัน toggle_option_menu
circ_checkbox = tk.Checkbutton(settings_frame, text="Circle", variable=circ_var, command=lambda: toggle_option_menu("Circle"))  # สร้าง checkbox สำหรับการเลือกวาดวงกลมและเรียกใช้ฟังก์ชัน toggle_option_menu เมื่อเลือกหรือลบการเลือก
circ_checkbox.grid(row=3, column=0, sticky="w", padx=5, pady=5)  # วาง checkbox ในตำแหน่งแถวที่ 3 คอลัมน์ที่ 0 พร้อมระยะห่างทางแนวนอนและแนวตั้ง
# สร้างเมนูเลือกขนาดสำหรับวงกลมและซ่อนเมนูเริ่มต้น
circ_size_menu = tk.OptionMenu(settings_frame, circ_size, "Radius=25", "Radius=50", "Radius=75")  # สร้างเมนูตัวเลือกขนาดของวงกลมพร้อมค่าตัวเลือกที่กำหนด
circ_size_menu.grid(row=3, column=1, padx=5, pady=5)  # วางเมนูตัวเลือกขนาดของวงกลมในตำแหน่งแถวที่ 3 คอลัมน์ที่ 1 พร้อมระยะห่าง
circ_size_menu.grid_remove()  # ซ่อนเมนูตัวเลือกขนาดของวงกลมจนกว่าจะถูกเลือกใน checkbox

# สร้างปุ่ม "Draw" เพื่อเรียกใช้ฟังก์ชัน draw_shapes เมื่อกดปุ่ม
draw_btn = tk.Button(root, text="Draw", command=draw_shapes)
draw_btn.pack(pady=5, padx=10)  # จัดวางปุ่ม "Draw" ด้วยระยะห่างแนวนอนและแนวตั้ง

# เริ่มต้น loop หลักของหน้าต่างเพื่อรับฟัง event และแสดงผล
root.mainloop()  # เริ่มการทำงานของหน้าต่างหลักเพื่อให้ GUI ทำงานและรอรับคำสั่งจากผู้ใช้

