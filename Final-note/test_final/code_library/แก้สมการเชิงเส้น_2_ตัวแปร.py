# โปรแกรมแก้สมการเชิงเส้น 2 ตัวแปร
# การแก้สมการเชิงเส้น 2 ตัวแปร
def solve_linear_equations(a1, b1, c1, a2, b2, c2):
    # ใช้สูตรการแก้สมการเชิงเส้น
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None, None  # ไม่มีคำตอบหรือคำตอบไม่ชัดเจน
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return x, y

# รับค่าจากผู้ใช้
print("แก้สมการเชิงเส้น 2 ตัวแปร:")
a1, b1, c1 = map(float, input("สมการที่ 1 (ใส่ค่า a1 b1 c1): ").split())
a2, b2, c2 = map(float, input("สมการที่ 2 (ใส่ค่า a2 b2 c2): ").split())

x, y = solve_linear_equations(a1, b1, c1, a2, b2, c2)
if x is None and y is None:
    print("สมการไม่มีคำตอบหรือคำตอบไม่ชัดเจน")
else:
    print(f"คำตอบคือ x = {x:.2f}, y = {y:.2f}")