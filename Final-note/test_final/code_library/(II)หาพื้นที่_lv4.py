# โปรแกรมคำนวณพื้นที่ของสามเหลี่ยม, สี่เหลี่ยม, ด้านยาวของสามเหลี่ยมมุมฉาก, สมการกำลังสอง, ระยะห่างระหว่างจุด
import math

# ฟังก์ชันคำนวณพื้นที่ของสามเหลี่ยมในกรณีต่างๆ (พีระมิด, การคำนวณด้วยซับซ้อน)
def Area_Of_Triangle(*dimensions):
    results = []
    for dimension in dimensions:
        if isinstance(dimension, tuple) and len(dimension) == 2:  # ตรวจสอบว่าเป็น tuple 2 ค่า (ฐาน, ความสูง)
            b, h = dimension
            if b <= 0 or h <= 0:
                results.append(f"Invalid dimensions for base {b} and height {h}. Both must be positive numbers.")
            else:
                area = 0.5 * b * h
                results.append(f"Base = {b}, Height = {h}, Area = {area:.2f}")
        elif isinstance(dimension, tuple) and len(dimension) == 3:  # กรณีสำหรับการคำนวณสามเหลี่ยมมุมฉากจากด้านทั้งสาม
            a, b, c = dimension
            if a <= 0 or b <= 0 or c <= 0:
                results.append(f"Invalid dimensions for sides {a}, {b}, {c}. All sides must be positive numbers.")
            else:
                semi_perimeter = (a + b + c) / 2
                area = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
                results.append(f"Sides = ({a}, {b}, {c}), Area = {area:.2f}")
        else:
            results.append(f"Invalid input: {dimension}. Expected a tuple of two or three values.")
    return results

# ฟังก์ชันคำนวณพื้นที่ของสี่เหลี่ยมในกรณีต่างๆ
def Area_Of_Rectangle(*dimensions):
    results = []
    for dimension in dimensions:
        if isinstance(dimension, tuple) and len(dimension) == 2:  # ตรวจสอบว่าเป็น tuple 2 ค่า (ยาว, กว้าง)
            l, w = dimension
            if l <= 0 or w <= 0:
                results.append(f"Invalid dimensions for length {l} and width {w}. Both must be positive numbers.")
            else:
                area = l * w
                results.append(f"Length = {l}, Width = {w}, Area = {area:.2f}")
        else:
            results.append(f"Invalid input: {dimension}. Expected a tuple of two values.")
    return results

# ฟังก์ชันคำนวณด้านยาวของสามเหลี่ยมมุมฉาก พร้อมทั้งเช็คกรณีที่ค่าด้านไม่ถูกต้อง
def The_Long_Side_Of_The_Right_Triangle(*sides):
    results = []
    for side in sides:
        if len(side) != 2:
            results.append(f"Invalid input: {side}. Expected a tuple of two sides.")
            continue
        a, b = side
        if a <= 0 or b <= 0:
            results.append(f"Both sides must be positive numbers: {a}, {b}")
        else:
            longside = math.sqrt(a**2 + b**2)
            results.append(f"Sides = ({a}, {b}), Longest side = {longside:.2f}")
    return results

# ฟังก์ชันคำนวณคำตอบของสมการกำลังสอง
def The_Solution_Of_Quadratic_Formula(*equations):
    results = []
    for a2, b2, c2 in equations:
        if a2 == 0:
            results.append(f"Invalid equation for a = 0: {a2}, b = {b2}, c = {c2}. 'a' must be non-zero.")
            continue

        discriminant = b2**2 - 4 * a2 * c2
        if discriminant < 0:
            root1 = (-b2 + complex(0, math.sqrt(-discriminant))) / (2 * a2)
            root2 = (-b2 - complex(0, math.sqrt(-discriminant))) / (2 * a2)
            results.append(f"Equation: a = {a2}, b = {b2}, c = {c2}, Solutions: x1 = {root1}, x2 = {root2}")
        elif discriminant == 0:
            x = -b2 / (2 * a2)
            results.append(f"Equation: a = {a2}, b = {b2}, c = {c2}, Single solution: x = {x:.2f}")
        else:
            x1 = (-b2 + math.sqrt(discriminant)) / (2 * a2)
            x2 = (-b2 - math.sqrt(discriminant)) / (2 * a2)
            results.append(f"Equation: a = {a2}, b = {b2}, c = {c2}, Solutions: x1 = {x1:.2f}, x2 = {x2:.2f}")
    return results

# ฟังก์ชันคำนวณระยะทางระหว่างจุดที่สามารถรับข้อมูลในรูปแบบ 2D หรือ 3D
def Distance_Between_Points(*points):
    results = []
    for p1, p2 in points:
        if len(p1) != len(p2):
            results.append(f"Points must have the same dimension: {p1} and {p2}")
            continue
        distance = math.sqrt(sum((p2[i] - p1[i])**2 for i in range(len(p1))))
        results.append(f"Distance between points {p1} and {p2} is {distance:.2f}")
    return results

# ฟังก์ชันแสดงผลลัพธ์ที่คำนวณจากฟังก์ชันต่างๆ
def display_results(title, results):
    print(f"\n{'-'*50}\n{title}\n{'-'*50}")
    for result in results:
        print(result)

# เริ่มต้นโปรแกรม
def main():
    print("Welcome to the Advanced Geometry Calculator!")
    
    # คำนวณพื้นที่สามเหลี่ยม
    triangles = [(3, 4), (5, 12, 13), (6, 8)]  # สามเหลี่ยมฐานสูงและสามเหลี่ยมมุมฉาก
    display_results("Area Of Triangle", Area_Of_Triangle(*triangles))

    # คำนวณพื้นที่สี่เหลี่ยม
    rectangles = [(4, 5), (7, 10)]  # สี่เหลี่ยม
    display_results("Area Of Rectangle", Area_Of_Rectangle(*rectangles))

    # หาด้านยาวสามเหลี่ยมมุมฉาก
    right_triangles = [(3, 4), (5, 12)]  # สามเหลี่ยมมุมฉาก
    display_results("Longest Side of Right Triangle", The_Long_Side_Of_The_Right_Triangle(*right_triangles))

    # คำนวณสมการกำลังสอง
    quadratics = [(1, -3, 2), (1, 2, 1), (1, -2, 5)]  # สมการกำลังสอง
    display_results("Quadratic Solutions", The_Solution_Of_Quadratic_Formula(*quadratics))

    # คำนวณระยะห่างระหว่างจุดใน 2D และ 3D
    points = [((1, 2), (4, 6)), ((1, 2, 3), (4, 5, 6))]  # จุดใน 2D และ 3D
    display_results("Distance Between Points", Distance_Between_Points(*points))

# เรียกโปรแกรมหลัก
if __name__ == "__main__":
    main()
