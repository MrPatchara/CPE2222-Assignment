import math
# โดยปกติ Python จะไม่ทำให้เกิด FloatingPointError เอง ดังนั้นต้องใช้ `math.error` เพื่อช่วย
math.error = FloatingPointError

try:
    # ตัวอย่างการคำนวณที่อาจทำให้เกิด FloatingPointError
    result = 1.0 / 0.0  # การหารด้วยศูนย์ที่เป็นทศนิยม
except FloatingPointError as e:
    print("เกิดข้อผิดพลาด:", e)
    print("ไม่สามารถคำนวณการหารด้วยศูนย์ในระบบจุดทศนิยมได้")

# โค้ดด้านล่างนี้ทำงานปกติหากไม่มีข้อผิดพลาด
print("โปรแกรมดำเนินการต่อ")
