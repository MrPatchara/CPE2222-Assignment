# โปรแกรมตัวอย่างการตรวจจับข้อผิดพลาด (Error) แต่ละประเภท
print("กรุณากรอก input ตามนี้เพื่อตรวจสอบข้อผิดพลาดแต่ละประเภท:")
print("1. TypeError: กรอก 1 + 'a'")
print("2. KeyError: กรอก 'jack' (เพื่อใช้เป็น key ใน dictionary ที่ไม่มี key นี้)")
print("3. NameError: กรอก 'A' (เพื่อใช้ตัวแปรที่ยังไม่ได้ประกาศ)")
print("4. IndexError: กรอก 0 (เพื่อเข้าถึง index ที่ไม่มีใน list ที่ว่าง)")
print("5. ValueError: กรอก '20.5abc' (เพื่อแปลง string ที่มีตัวอักษรเป็น integer)")
print("\nหมายเหตุ: กรอก input ตามที่ระบุไว้เพื่อดูการเกิด Exception และวิธีการตรวจจับข้อผิดพลาด")

# 1. TypeError - เกิดจากการใช้ตัวแปรประเภทที่ไม่ถูกต้อง (เช่น การบวก string กับ integer)
try:
    user_input = input("กรอก 1 + 'a' เพื่อตรวจสอบ TypeError: ")
    result = 1 + user_input  # จะเกิด TypeError หาก user_input ไม่ใช่ integer
except TypeError as e:
    print("Escaping TypeError:", e ,"\n")

# 2. KeyError - เกิดเมื่อพยายามเข้าถึง key ที่ไม่มีใน dictionary
try:
    data = {"name": "Alice"}
    key = input("กรอก key ที่ไม่มีใน dictionary เช่น 'jack' เพื่อตรวจสอบ KeyError: ")
    print(data[key])  # จะเกิด KeyError หาก key ไม่มีใน dictionary
except KeyError as e:
    print("Escaping KeyError:", e ,"\n")

# 3. NameError - เกิดจากการใช้ตัวแปรที่ยังไม่ได้ประกาศ
try:
    var_name = input("กรอกชื่อของตัวแปรที่ยังไม่ได้ประกาศ เช่น 'A' เพื่อตรวจสอบ NameError: ")
    print(eval(var_name))  # จะเกิด NameError หาก var_name ไม่มีอยู่จริง
except NameError as e:
    print("Escaping NameError:", e ,"\n")

# 4. IndexError - เกิดเมื่อพยายามเข้าถึง index ที่อยู่นอกขอบเขตของ list
try:
    my_list = []  # กำหนด list ที่ว่าง
    index = int(input("กรอก index ที่ไม่มีใน list ว่าง เช่น 0 เพื่อตรวจสอบ IndexError: "))
    print(my_list[index])  # จะเกิด IndexError หาก list ไม่มี index ที่กรอก
except IndexError as e:
    print("Escaping IndexError:", e ,"\n")

# 5. ValueError - เกิดเมื่อพยายามแปลง string ที่ไม่ใช่ตัวเลขให้เป็น integer
try:
    user_input = input("กรอกค่าที่ไม่ใช่ตัวเลข เช่น '20.5abc' เพื่อตรวจสอบ ValueError: ")
    number = int(user_input)  # จะเกิด ValueError หาก user_input ไม่สามารถแปลงเป็น integer ได้
except ValueError as e:
    print("Escaping ValueError:", e ,"\n")
