import math
import matplotlib.pyplot as plt

# ฟังก์ชันคำนวณพื้นที่และปริมาตรของทรงกลม
def circle_and_sphere_calculations(radius):
    if radius <= 0:
        return "Radius must be greater than 0."
    # พื้นที่วงกลม
    circle_area = math.pi * radius**2
    # ปริมาตรทรงกลม
    sphere_volume = (4/3) * math.pi * radius**3
    return f"Circle Area = {circle_area:.2f}, Sphere Volume = {sphere_volume:.2f}"

# ฟังก์ชันคำนวณระยะห่างใน 3 มิติ
def distance_3d(x1, y1, z1, x2, y2, z2):
    # ระยะทางใน 3 มิติ
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return f"Distance in 3D = {distance:.2f}"

# ฟังก์ชันคำนวณความลาดเอียงระหว่างสองจุด
def slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)."
    slope_value = (y2 - y1) / (x2 - x1)
    return f"Slope = {slope_value:.2f}"

# ฟังก์ชันวาดกราฟสมการกำลังสอง
def plot_quadratic(a, b, c):
    if a == 0:
        return "Coefficient 'a' must not be zero."
    # สร้างช่วงของ x สำหรับกราฟ
    x = [i / 10 for i in range(-100, 101)]  # -10 ถึง 10 (เพิ่มความละเอียด)
    # คำนวณค่า y ตามสมการ ax^2 + bx + c
    y = [a*i**2 + b*i + c for i in x]
    # วาดกราฟ
    plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
    plt.axhline(0, color='black', linewidth=0.5)  # เส้นแกน x
    plt.axvline(0, color='black', linewidth=0.5)  # เส้นแกน y
    plt.title("Graph of Quadratic Equation")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()
    return "Graph plotted successfully."

# เมนูหลักของโปรแกรม
def main():
    while True:
        print("\n=== Advanced Math Calculations Menu ===")
        print("1. Circle Area and Sphere Volume")
        print("2. Distance in 3D Space")
        print("3. Slope Between Two Points")
        print("4. Plot Quadratic Equation")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            # รับข้อมูลสำหรับรัศมี
            try:
                radius = float(input("Enter the radius: "))
                print(circle_and_sphere_calculations(radius))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == 2:
            # รับข้อมูลสำหรับจุดใน 3 มิติ
            try:
                x1 = float(input("Enter x1: "))
                y1 = float(input("Enter y1: "))
                z1 = float(input("Enter z1: "))
                x2 = float(input("Enter x2: "))
                y2 = float(input("Enter y2: "))
                z2 = float(input("Enter z2: "))
                print(distance_3d(x1, y1, z1, x2, y2, z2))
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == 3:
            # รับข้อมูลสำหรับคำนวณความลาดเอียง
            try:
                x1 = float(input("Enter x1: "))
                y1 = float(input("Enter y1: "))
                x2 = float(input("Enter x2: "))
                y2 = float(input("Enter y2: "))
                print(slope(x1, y1, x2, y2))
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == 4:
            # รับข้อมูลสำหรับสมการกำลังสอง
            try:
                a = float(input("Enter coefficient a: "))
                b = float(input("Enter coefficient b: "))
                c = float(input("Enter constant c: "))
                print(plot_quadratic(a, b, c))
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")

# เรียกใช้โปรแกรมหลัก
if __name__ == "__main__":
    main()
