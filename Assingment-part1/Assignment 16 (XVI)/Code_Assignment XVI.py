# Assignment 16 (XVI) 
import math # นำเข้าโมดูล math 

# สร้าง dict ชื่อ shapes โดยมี key เป็นชื่อรูปทรง และ value เป็น dict ที่มี key เป็นความยาวของรัศมีหรือด้านของรูปทรง และ value เป็นพื้นที่ของรูปทรงนั้น
shapes = {
    "circle": {r: round(math.pi * r**2, 2) for r in range(1, 101)},
    "square": {l: l**2 for l in range(1, 101)},
    "triangle": {l: round((math.sqrt(3) / 4) * l**2, 2) for l in range(1, 101)}
}

# สร้าง loop โดยให้ loop นี้ทำงานไปเรื่อยๆ จนกว่าจะมีการ break ออกจาก loop
while True:
    # รับค่า input จากผู้ใช้ โดยให้ผู้ใช้ใส่ชื่อรูปทรง
    shape = input("Enter the geometry shape for an area calculation\n[Circle, Square, Triangle]\n[Enter something else to exit this program]: ").strip().lower()
    
    # ตรวจสอบว่ารูปทรงที่ผู้ใช้ใส่มีอยู่ใน dict shapes หรือไม่
    if shape not in shapes: # ถ้าไม่มีให้แสดงข้อความว่า "Exiting program..." และ break ออกจาก loop
        print("Exiting program...")
        break
    try: 
        index = int(float(input("Enter the dictionary key [1 - 100]: "))) # รับค่า input จากผู้ใช้ โดยให้ผู้ใช้ใส่ค่า index ที่ต้องการหาพื้นที่ของรูปทรง
    except ValueError: 
        print("Invalid input. Please enter a number.") 
        continue

    # ตรวจสอบว่าค่า index ที่ผู้ใช้ใส่อยู่ในช่วง 1 - 100 หรือไม่
    if 1 <= index <= 100:
        # แสดงข้อความว่า "The area of {ชื่อรูปทรง} is {พื้นที่ของรูปทรง}" โดยใช้ f-string
        area = shapes[shape][index] # หาค่าพื้นที่ของรูปทรงโดยใช้ค่า index ที่ผู้ใช้ใส่
        print(f"The area of {shape.upper()} is {area}") 
    else:
        print("!!! The key is out of scope !!!")
        break
