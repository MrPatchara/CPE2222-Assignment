# โปรแกรมคำนวณเรื่องเรขาคณิตระดับสูง โดยใช้
import math

# ฟังก์ชันคำนวณพื้นที่สามเหลี่ยม พร้อมรองรับหลายชุดข้อมูล
def Area_Of_Triangle(*dimensions):
    results = []
    for b, h in dimensions:
        if b <= 0 or h <= 0:
            results.append("Base and Height must be positive numbers.")
        else:
            aot = 0.5 * b * h
            results.append(f"Base = {b}, Height = {h}, Area = {aot:.2f}")
    return results

# ฟังก์ชันคำนวณพื้นที่สี่เหลี่ยม และเพิ่มการรองรับการคำนวณหลายครั้ง
def Area_Of_Rectangle(*pairs):
    results = []
    for l, w in pairs:
        if l <= 0 or w <= 0:
            results.append("Length and Width must be positive numbers.")
        else:
            aor = l * w
            results.append(f"Length = {l}, Width = {w}, Area = {aor:.2f}")
    return results

# ฟังก์ชันหาด้านยาวของสามเหลี่ยมมุมฉาก พร้อมเช็คกรณีไม่มีคำตอบ
def The_Long_Side_Of_The_Right_Triangle(a1, b1):
    if a1 <= 0 or b1 <= 0:
        return "Both sides must be positive numbers."
    longside = math.sqrt(a1**2 + b1**2)
    return f"The longest side is {longside:.2f}"

# ฟังก์ชันคำนวณสมการกำลังสอง รองรับกรณีมีหลายสมการ
def The_Solution_Of_Quadratic_Formula(*coefficients):
    results = []
    for c2, b2, a2 in coefficients:
        if a2 == 0:
            results.append("Coefficient 'a' must not be zero.")
            continue

        discriminant = b2**2 - 4 * a2 * c2
        if discriminant < 0:
            root1 = (-b2 + complex(0, math.sqrt(-discriminant))) / (2 * a2)
            root2 = (-b2 - complex(0, math.sqrt(-discriminant))) / (2 * a2)
            results.append(f"a={a2}, b={b2}, c={c2}, Solutions: x1={root1}, x2={root2}")
        elif discriminant == 0:
            x1 = -b2 / (2 * a2)
            results.append(f"a={a2}, b={b2}, c={c2}, Single solution: x={x1}")
        else:
            x1 = (-b2 + math.sqrt(discriminant)) / (2 * a2)
            x2 = (-b2 - math.sqrt(discriminant)) / (2 * a2)
            results.append(f"a={a2}, b={b2}, c={c2}, Solutions: x1={x1:.2f}, x2={x2:.2f}")
    return results

# ฟังก์ชันคำนวณระยะทางระหว่างสองจุดใน 2D หรือ 3D
def Distance_Between_Points(p1, p2):
    if len(p1) != len(p2):
        return "Points must have the same dimensions."
    distance = math.sqrt(sum((p2[i] - p1[i])**2 for i in range(len(p1))))
    return f"The distance between points {p1} and {p2} is {distance:.2f}"

# ฟังก์ชันแสดงผลลัพธ์ทุกฟังก์ชันในรูปแบบข้อความที่เข้าใจง่าย
def display_results(title, results):
    print(f"\n{'-'*50}\n{title}\n{'-'*50}")
    for result in results:
        print(result)

# เริ่มต้นโปรแกรม
def main():
    print("Welcome to the Advanced Geometry Calculator!")
    
    # คำนวณพื้นที่สามเหลี่ยม
    triangles = [(3, 4), (5, 10), (7, -2)]  # ทดสอบหลายค่า
    display_results("Area Of Triangle", Area_Of_Triangle(*triangles))

    # คำนวณพื้นที่สี่เหลี่ยม
    rectangles = [(4, 5), (3, 7), (-2, 5)]  # ทดสอบหลายค่า
    display_results("Area Of Rectangle", Area_Of_Rectangle(*rectangles))

    # หาด้านยาวสามเหลี่ยมมุมฉาก
    print("\nFinding the longest side of a right triangle:")
    print(The_Long_Side_Of_The_Right_Triangle(3, 4))

    # คำนวณสมการกำลังสอง
    quadratics = [(1, -3, 2), (1, 2, 1), (1, 0, -4)]  # ทดสอบหลายสมการ
    display_results("Solutions Of Quadratic Formula", The_Solution_Of_Quadratic_Formula(*quadratics))

    # ระยะห่างระหว่างจุดใน 2D และ 3D
    print("\nCalculating distances:")
    print(Distance_Between_Points((1, 2), (4, 6)))  # 2D
    print(Distance_Between_Points((1, 2, 3), (4, 6, 8)))  # 3D

# เรียกโปรแกรมหลัก
if __name__ == "__main__":
    main()
