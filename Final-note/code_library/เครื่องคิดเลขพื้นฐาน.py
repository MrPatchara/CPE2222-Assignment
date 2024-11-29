#โปรแกรมเครื่องคิดเลขที่สามารถบวก ลบ คูณ และหาร
def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "หารด้วยศูนย์ไม่ได้"
        return a / b
    else:
        return "ตัวดำเนินการไม่ถูกต้อง"

# รับข้อมูลจากผู้ใช้
a = float(input("ใส่ตัวเลขที่ 1: "))
b = float(input("ใส่ตัวเลขที่ 2: "))
operator = input("ใส่ตัวดำเนินการ (+, -, *, /): ")

result = calculate(a, b, operator)
print(f"ผลลัพธ์: {result}")