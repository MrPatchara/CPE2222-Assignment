# โปรแกรมคำนวณพื้นที่ของรูปสามเหลี่ยม สี่เหลี่ยม ความยาวด้านที่ยาวที่สุดของสามเหลี่ยมมุมฉาก สมการกระจาย ระยะห่างระหว่างจุดสองจุด
import math

#ส่งพร้อมโค้ด
def Area_Of_Triangle(b, h):
    aot = 0.5 * b * h
    return f"The area is {aot:.2f}"

def Area_Of_Rectangle(l, w):
    aor = l * w
    return f"The area is {aor:.2f}"

def The_Long_Side_Of_The_Right_Triangle(a1, b1):
    longside = math.sqrt(a1**2 + b1**2)
    return f"The length of the longest size is {longside:.2f}"

def The_Solution_Of_Quadratic_Formula(c2, b2, a2):
    if a2 == 0:
        return "ค่า a ต้องไม่เท่ากับ 0"

    discriminant = b2**2 - 4 * a2 * c2

    if discriminant < 0:
        # กรณีที่มีค่าติดลบ จะเป็นจำนวนเชิงซ้อน
        root1 = (-b2 + complex(0, math.sqrt(-discriminant))) / (2 * a2)
        root2 = (-b2 - complex(0, math.sqrt(-discriminant))) / (2 * a2)
        return f"The 1st solution is x = {root1}\nThe 2nd solution is x = {root2}"
    elif discriminant == 0:
        x1 = -b2 / (2 * a2)
        x2 = -b2 / (2 * a2)
        return f"The 1st solution is x = {x1}\nThe 2nd solution is x = {x2}"
    else:
        x1 = (-b2 + math.sqrt(discriminant)) / (2 * a2)
        x2 = (-b2 - math.sqrt(discriminant)) / (2 * a2)
        return f"The 1st solution is x = {x1}\nThe 2nd solution is x = {x2}"

def Distance_Of_Two_Points(x1, y1, x2, y2):
    dtp = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return f"The distance between the two points is {dtp:.2f}"

print("##################################################")
print("                 Area Of Triangle                 ")
print("--------------------------------------------------")
b = float(input("Enter Base: "))
h = float(input("Enter Height: "))
print(Area_Of_Triangle(b, h))

print("--------------------------------------------------")
print("                 Area Of Rectangle                 ")
print("--------------------------------------------------")
l = float(input("Enter Length: "))
w = float(input("Enter Width: "))
print(Area_Of_Rectangle(l, w))

print("--------------------------------------------------")
print("       The Long Side Of The Right Triangle        ")
print("--------------------------------------------------")
a1 = float(input("Enter length of the 1st side: "))
b1 = float(input("Enter length of the 2nd side: "))
print(The_Long_Side_Of_The_Right_Triangle(a1, b1))

print("--------------------------------------------------")
print("        The Solution Of Quadratic Formula         ")
print("--------------------------------------------------")
c2 = float(input("Enter Constant(c): "))
b2 = float(input("Enter Coefficient of Linear Term (b): "))
a2 = float(input("Enter Coefficient of Quadratic Term (a): "))
print(The_Solution_Of_Quadratic_Formula(c2, b2, a2))

print("--------------------------------------------------")
print("             Distance Of Two Points               ")
print("--------------------------------------------------")
x1 = float(input("Enter x of the 1st point: "))
y1 = float(input("Enter y of the 1st point: "))
x2 = float(input("Enter x of the 2nd point: "))
y2 = float(input("Enter y of the 2nd point: "))
print(Distance_Of_Two_Points(x1, y1, x2, y2))
