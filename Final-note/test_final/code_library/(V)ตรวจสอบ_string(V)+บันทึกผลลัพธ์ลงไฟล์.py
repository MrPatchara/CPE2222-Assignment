# โปรแกรมนี้เป็นโปรแกรมที่ใช้ในการคำนวณข้อมูลของสตริง โดยจะรับข้อมูลสตริง 2 ตัวจากผู้ใช้
# โค้ดนี้เพิ่มการ บันทึกผลลัพธ์ลงไฟล์ (ในไฟล์ .txt) นอกจากการแสดงผลบนหน้าจอ 
# โดยผลลัพธ์ทั้งหมดจะถูกบันทึกลงในไฟล์ชื่อ result.txt ซึ่งสามารถเปิดดูในภายหลังได้
# รับข้อมูลจากผู้ใช้
user_a = input('Enter string A: ')
user_b = input('Enter string B: ')

# แปลง String เป็นเซ็ต
set_a = set(user_a)
set_b = set(user_b)

# คำนวณผลลัพธ์
output = {
    "Unique characters in A": len(set_a),
    "Unique characters in B": len(set_b),
    "Characters in both": set_a & set_b,
    "Characters in A not in B": set_a - set_b,
    "Characters in B not in A": set_b - set_a,
    "Symmetric difference": set_a ^ set_b,
    "Union": set_a | set_b
}

# แสดงผลและบันทึกลงไฟล์
print('--------------------------------------------------')
with open("result.txt", "w", encoding="utf-8") as file:
    for key, value in output.items():
        file.write(f'{key}: {value}\n')
        print(f'{key}: {value}')
print("Results saved to result.txt")