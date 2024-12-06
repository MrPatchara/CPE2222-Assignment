# โปรแกรมนี้เป็นโปรแกรมที่ใช้ในการคำนวณข้อความที่ผู้ใช้ป้อนเข้ามา
# ค้ดนี้แปลงข้อความที่ผู้ใช้ป้อนให้เป็น ตัวพิมพ์เล็กทั้งหมด (lowercase) 
# เพื่อหลีกเลี่ยงการเปรียบเทียบที่แตกต่างจากตัวพิมพ์ใหญ่และตัวพิมพ์เล็ก (case-sensitive) เช่น "A" กับ "a" จะถือเป็นตัวอักษรเดียวกัน
# รับข้อมูลจากผู้ใช้ พร้อมแปลงเป็น lower case เพื่อจัดการกรณี sensitivity
user_a = input('Please enter the string A: ').lower()
user_b = input('Please enter the string B: ').lower()

# แปลง String เป็นเซ็ตเพื่อคำนวณ
set_a = set(user_a)
set_b = set(user_b)

print('--------------------------------------------------')
# คำนวณและแสดงผลลัพธ์
print(f'Number of unique characters in A: {len(set_a)}')
print(f'Number of unique characters in B: {len(set_b)}')
print(f'Number of common characters in both A and B: {len(set_a & set_b)}')
print(f'Characters in A but not in B: {set_a - set_b}')
print(f'Characters in B but not in A: {set_b - set_a}')
print(f'Characters in A or B but not both: {set_a ^ set_b}')
print(f'All unique characters in A or B: {set_a | set_b}')
