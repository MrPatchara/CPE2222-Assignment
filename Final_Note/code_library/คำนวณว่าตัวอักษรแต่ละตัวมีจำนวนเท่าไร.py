#โค้ดนี้ใช้ Counter จากโมดูล collections เพื่อทำการนับจำนวนของตัวอักษรแต่ละตัวในข้อความของผู้ใช้ (จะคำนวณว่าตัวอักษรแต่ละตัวมีจำนวนเท่าไร) 
# และแสดงผลนับตัวอักษรที่ซ้ำซ้อน
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
