# Assignment II: Basic Math Formulas
import math #ใช้ไลบรารี math 
#ฟังก์ชันคำนวณพื้นที่ของสามเหลี่ยม
def area_of_triangle():
    print(f"{'Area of Triangle':^50}")
    print("-"*50)
    base = float(input("Enter Base: "))
    height = float(input("Enter Height: "))
    area = 0.5 * base * height
    #print(f"The area is {area:.2f}")
    print(f"The area is {area}")  #optional ถ้าต้องการให้แสดงทศนิยม 1 ตำแหน่ง
    
# ฟังก์ชันคำนวณพื้นที่ของสี่เหลี่ยมผืนผ้า
def area_of_rectangle():
    print(f"{'Area of Rectangle':^50}") 
    print("-"*50)
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))
    area = length * width
    #ปริ้นค่าพื้นที่ ทศนิยม 2 ตำแหน่ง
    #print(f"The area is {area:.2f}")
    print(f"The area is {area}")
    
def longest_side_of_right_triangle():
    print(f"{'The Longest Size of Right Triangle':^50}") 
    print("-"*50)
    a = float(input("Enter length of the 1st side: "))
    b = float(input("Enter length of the 2nd side: "))
    c = math.sqrt(a**2 + b**2) #ใช้ math.sqrt เพื่อคำนวณรากที่สองของผลรวมของ a กำลังสอง และ b กำลังสอง
    #print(f"The length of the longest size is {c:.2f}")
    print(f"The area is {c}")
    
#ฟังก์ชันคำนวณสูตรกำลังสอง
def quadratic_formula():
    print(f"{'The Solution of Quadratic Formula':^50}") #ใช้ f-string ในการปริ้นหัวข้อเพื่อให้อยู่ตรงกลาง
    print("-"*50)
    c = float(input("Enter Constant (\"c\"): "))
    b = float(input("Enter Coefficient of Linear Term (\"b\"): "))
    a = float(input("Enter Coefficient of Quadratic Term (\"a\"): "))
    discriminant = b**2 - 4 * a * c

    if discriminant < 0: 
        discriminant = complex(discriminant, 0) # ใช้ complex ในการรับค่าที่เป็นเลขเชิงซ้อน

    x1 = (-b + discriminant**0.5) / (2 * a) 
    x2 = (-b - discriminant**0.5) / (2 * a) 

    print(f"The 1st solution is x = {x1}")
    print(f"The 2nd solution is x = {x2}")

#ฟังก์ชันคำนวณระยะห่างระหว่าง 2 จุด
def distance_between_points():
    print(f"{'Distance of 2 Points':^50}") #ใช้ f-string ในการปริ้นหัวข้อเพื่อให้อยู่ตรงกลาง
    print("-"*50)
    #รับค่าพิกัด x1, y1 สำหรับจุดแรก และ x2, y2 สำหรับจุดที่สอง
    x1 = float(input("Enter x of the 1st point: "))
    y1 = float(input("Enter y of the 1st point: "))
    x2 = float(input("Enter x of the 2nd point: "))
    y2 = float(input("Enter y of the 2nd point: "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    #print(f"The distance is {distance:.2f}")
    print(f"The distance is {distance}")    

#เรียกใช้งานฟังก์ชันทั้งหมดและแสดงหัวข้อหลัก "Basic Math Formulas" โดยจัดให้อยู่กลางบรรทัด
print(f"{'Basic Math Formulas':^50}") #ใช้ f-string ในการปริ้นหัวข้อเพื่อให้อยู่ตรงกลาง
print("#"*50)
area_of_triangle()
print("-"*50)
area_of_rectangle()
print("-"*50)
longest_side_of_right_triangle()
print("-"*50)
quadratic_formula()
print("-"*50)
distance_between_points()
print("-"*50)
