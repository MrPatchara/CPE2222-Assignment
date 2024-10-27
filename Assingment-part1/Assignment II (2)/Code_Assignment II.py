import math

def area_of_triangle():
    print("                 Area of Triangle                   ")
    print("--------------------------------------------------")
    base = float(input("Enter Base: "))
    height = float(input("Enter Height: "))
    area = 0.5 * base * height
    print(f"The area is {area:.2f}")
    

def area_of_rectangle():
    print("                 Area of Rectangle                  ")
    print("--------------------------------------------------")
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))
    area = length * width
    #ปริ้นค่าพื้นที่ ทศนิยม 2 ตำแหน่ง
    print(f"The area is {area:.2f}")

def longest_side_of_right_triangle():
    print("        The Longest Size of Right Triangle"          )
    print("--------------------------------------------------")
    a = float(input("Enter length of the 1st side: "))
    b = float(input("Enter length of the 2nd side: "))
    c = math.sqrt(a**2 + b**2)
    print(f"The length of the longest size is {c:.2f}")
  

def quadratic_formula():
    print("          The Solution of Quadratic Formula         ")
    print("--------------------------------------------------")
    c = float(input("Enter Constant (\"c\"): "))
    b = float(input("Enter Coefficient of Linear Term (\"b\"): "))
    a = float(input("Enter Coefficient of Quadratic Term (\"a\"): "))
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        discriminant = complex(discriminant, 0)

    # ใช้ cmath.sqrt เพื่อรองรับรากเชิงซ้อน
    x1 = (-b + discriminant**0.5) / (2 * a)
    x2 = (-b - discriminant**0.5) / (2 * a)

    print(f"The 1st solution is x = {x1}")
    print(f"The 2nd solution is x = {x2}")


def distance_between_points():
    print("               Distance of 2 Points                 ")
    print("--------------------------------------------------")
    x1 = float(input("Enter x of the 1st point: "))
    y1 = float(input("Enter y of the 1st point: "))
    x2 = float(input("Enter x of the 2nd point: "))
    y2 = float(input("Enter y of the 2nd point: "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"The distance is {distance:.2f}")
    

print("                Basic Math Formulas        ")
print("##################################################")
area_of_triangle()
print("--------------------------------------------------")
area_of_rectangle()
print("--------------------------------------------------")
longest_side_of_right_triangle()
print("--------------------------------------------------")
quadratic_formula()
print("--------------------------------------------------")
distance_between_points()
print("--------------------------------------------------")
