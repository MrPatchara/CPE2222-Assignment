# โปรแกรมคำนวณพื้นที่และเส้นรอบรูปของรูปสามเหลี่ยม พื้นที่ เส้นรอบรูป และเส้นทแยงมุมของรูปสี่เหลี่ยมผืนผ้า ระยะทางและจุดกึ่งกลางระหว่างสองจุด และแก้สมการกำลังสอง
import math

# ฟังก์ชันคำนวณพื้นที่และเส้นรอบรูปของรูปสามเหลี่ยม
def triangle_area_and_perimeter(base, height, side1, side2):
    # คำนวณพื้นที่สามเหลี่ยม
    area = 0.5 * base * height
    # คำนวณเส้นรอบรูปสามเหลี่ยม
    perimeter = base + side1 + side2
    return f"Area = {area:.2f}, Perimeter = {perimeter:.2f}"

# ฟังก์ชันคำนวณพื้นที่ เส้นรอบรูป และเส้นทแยงมุมของรูปสี่เหลี่ยมผืนผ้า
def rectangle_calculations(length, width):
    # พื้นที่
    area = length * width
    # เส้นรอบรูป
    perimeter = 2 * (length + width)
    # เส้นทแยงมุม (ใช้ทฤษฎีปีทาโกรัส)
    diagonal = math.sqrt(length**2 + width**2)
    return f"Area = {area:.2f}, Perimeter = {perimeter:.2f}, Diagonal = {diagonal:.2f}"

# ฟังก์ชันคำนวณระยะทางและจุดกึ่งกลางระหว่างสองจุด
def distance_and_midpoint(x1, y1, x2, y2):
    # ระยะทางระหว่างสองจุด
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # จุดกึ่งกลาง
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
    return f"Distance = {distance:.2f}, Midpoint = {midpoint}"

# ฟังก์ชันแก้สมการกำลังสอง พร้อมตรวจสอบประเภทของราก
def solve_quadratic(a, b, c):
    if a == 0:
        return "Coefficient 'a' must not be zero."

    # คำนวณ Discriminant
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        root_type = "Real and Distinct"
    elif discriminant == 0:
        root1 = root2 = -b / (2 * a)
        root_type = "Real and Equal"
    else:
        root1 = (-b + complex(0, math.sqrt(-discriminant))) / (2 * a)
        root2 = (-b - complex(0, math.sqrt(-discriminant))) / (2 * a)
        root_type = "Complex"
    
    return f"Roots: {root1}, {root2} (Type: {root_type})"

# ฟังก์ชันเมนูหลักของโปรแกรม
def main():
    while True:
        # แสดงเมนูให้ผู้ใช้เลือก
        print("\n=== Math Calculations Menu ===")
        print("1. Triangle Area and Perimeter")
        print("2. Rectangle Area, Perimeter, and Diagonal")
        print("3. Distance and Midpoint Between Two Points")
        print("4. Solve Quadratic Equation")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # รับข้อมูลสำหรับรูปสามเหลี่ยม
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            side1 = float(input("Enter the first side of the triangle: "))
            side2 = float(input("Enter the second side of the triangle: "))
            print(triangle_area_and_perimeter(base, height, side1, side2))

        elif choice == '2':
            # รับข้อมูลสำหรับรูปสี่เหลี่ยมผืนผ้า
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print(rectangle_calculations(length, width))

        elif choice == '3':
            # รับข้อมูลจุดสองจุด
            x1 = float(input("Enter x1: "))
            y1 = float(input("Enter y1: "))
            x2 = float(input("Enter x2: "))
            y2 = float(input("Enter y2: "))
            print(distance_and_midpoint(x1, y1, x2, y2))

        elif choice == '4':
            # รับข้อมูลสำหรับสมการกำลังสอง
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter constant c: "))
            print(solve_quadratic(a, b, c))

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# เรียกใช้โปรแกรมหลัก
if __name__ == "__main__":
    main()
