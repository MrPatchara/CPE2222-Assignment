# โปรแกรมนี้เป็นโค้ดที่ใช้ในการประมวลผลข้อมูลจากสตริง 2 ตัว โดยใช้ฟังก์ชัน
#โค้ดนี้เพิ่มการใช้ ฟังก์ชัน เพื่อทำให้โค้ดดูเป็นระเบียบและใช้งานได้ง่ายขึ้น โดยใช้ฟังก์ชัน process_strings() ที่คำนวณผลลัพธ์ทั้งหมด 
# จากนั้นใช้ dictionary ในการเก็บผลลัพธ์ของการคำนวณต่าง ๆ
def process_strings(a, b):
    # แปลง String เป็นเซ็ต
    set_a = set(a)
    set_b = set(b)

    # สร้างผลลัพธ์เป็น dictionary
    result = {
        "Unique in A": len(set_a),
        "Unique in B": len(set_b),
        "Common characters": set_a & set_b,
        "A not in B": set_a - set_b,
        "B not in A": set_b - set_a,
        "Symmetric difference": set_a ^ set_b,
        "Union": set_a | set_b
    }
    return result

# รับข้อมูลจากผู้ใช้ และอนุญาตตัวเลข
user_a = input('Please enter the string A (can include numbers): ')
user_b = input('Please enter the string B (can include numbers): ')

# เรียกใช้ฟังก์ชัน
output = process_strings(user_a, user_b)

# แสดงผลแบบจัดระเบียบ
print('--------------------------------------------------')
for key, value in output.items():
    print(f'{key}: {value}')
