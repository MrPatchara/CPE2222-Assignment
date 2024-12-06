# โปรแกรมนี้เป็นโปรแกรมที่ใช้ในการหาตัวอักษรที่ซ้ำกัน และ ตัวอักษรที่ไม่ซ้ำกัน ระหว่างสองข้อความที่ผู้ใช้ป้อนเข้ามา
# โค้ดนี้เพิ่มฟังก์ชัน clean_input() ที่จะ ลบตัวอักษรซ้ำ และ เอาช่องว่างออก จากข้อความที่ผู้ใช้ป้อน 
# (ใช้ set() เพื่อทำให้ข้อความไม่ซ้ำ) และรองรับการใช้งาน Unicode เพื่อให้สามารถใช้อักขระพิเศษหรือภาษาต่างประเทศได้
def clean_input(string):
    # เอาช่องว่างออก และลบตัวอักษรซ้ำ
    return "".join(set(string.strip()))

# รับข้อมูลจากผู้ใช้ พร้อมทำความสะอาด String
user_a = clean_input(input('Enter string A (Unicode supported): '))
user_b = clean_input(input('Enter string B (Unicode supported): '))

set_a = set(user_a)
set_b = set(user_b)

print('--------------------------------------------------')
print(f'Cleaned A: {user_a}')
print(f'Cleaned B: {user_b}')
print(f'Characters common in both: {set_a & set_b}')
print(f'Characters unique to A or B: {set_a ^ set_b}')
print(f'Total unique characters: {set_a | set_b}')