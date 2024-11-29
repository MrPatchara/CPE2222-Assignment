#โปรแกรมแก้สมการกำลังสองและหาคำตอบที่เป็นรากของสมการ
import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, None
    else:
        return None, None

# รับข้อมูลจากผู้ใช้
a = float(input("ใส่ค่าของ a: "))
b = float(input("ใส่ค่าของ b: "))
c = float(input("ใส่ค่าของ c: "))

roots = solve_quadratic(a, b, c)
if roots[0] is not None:
    if roots[1] is not None:
        print(f"รากของสมการคือ {roots[0]:.2f} และ {roots[1]:.2f}")
    else:
        print(f"รากของสมการคือ {roots[0]:.2f}")
else:
    print("สมการไม่มีคำตอบในจำนวนจริง")