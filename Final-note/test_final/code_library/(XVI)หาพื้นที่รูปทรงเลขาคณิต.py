# โปรแกรมคำนวณพื้นที่รูปทรงต่างๆ
import math

shape_areas = {
    "Circle": {i: round(math.pi * i ** 2, 2) for i in range(1, 101)}, # คำนวณพื้นที่ของวงกลม
    "Square": {i: i ** 2 for i in range(1, 101)}, # คำนวณพื้นที่ของสี่เหลี่ยม
    "Triangle": {i: round((math.sqrt(3) / 4) * i ** 2, 2) for i in range(1, 101)} # คำนวณพื้นที่ของสามเหลี่ยม
}

while True:
    shape = input("Enter shape (Circle, Square, Triangle): ").capitalize() # รับค่ารูปทรง
    if shape not in shape_areas: # ตรวจสอบว่ารูปทรงที่รับเข้ามามีอยู่ใน dictionary หรือไม่
        print("Shape not in dictionary.") 
        break

    try:
        index = int(float(input("Enter the dictionary key [1-100]: "))) # รับค่า index ของ dictionary
        if 1 <= index <= 100:
            print(f'-' * 50)
            print(f"The area of {shape} with index {index} is:", shape_areas[shape][index]) 
            print(f'-' * 50)
        else:
            break
    except ValueError:
        break
