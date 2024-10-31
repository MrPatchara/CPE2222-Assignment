# Assignment VIII: ข้อมูลของเกม Scrabble
scrabble = [
    'a', 1, 9, 4.8, 'b', 3, 2, 3.2, 'c', 3, 2, 3.2, 'd', 2, 4, 4.3, 'e', 1, 12, 6.4,
    'f', 4, 2, 4.3, 'g', 2, 3, 3.2, 'h', 4, 2, 4.3, 'i', 1, 9, 4.8, 'j', 8, 1, 4.3,
    'k', 5, 1, 2.7, 'l', 1, 4, 2.1, 'm', 3, 2, 3.2, 'n', 1, 6, 3.2, 'o', 1, 8, 4.3,
    'p', 3, 2, 3.2, 'q', 10, 1, 5.3, 'r', 1, 6, 3.2, 's', 1, 4, 2.1, 't', 1, 6, 3.2,
    'u', 1, 4, 2.1, 'v', 4, 2, 4.3, 'w', 4, 2, 4.3, 'x', 8, 1, 4.3, 'y', 4, 2, 4.3, 'z', 10, 1, 5.3
]
# ข้อมูลถูกจัดเก็บเป็นรายการ (list) ที่เก็บข้อมูลตัวอักษร คะแนน จำนวน และสัดส่วน


# แยกข้อมูลเป็นกลุ่ม [ตัวอักษร, คะแนน, จำนวน, สัดส่วน]
data = list(zip(scrabble[::4], scrabble[1::4], scrabble[2::4], scrabble[3::4]))
# ใช้ zip และการ slice เพื่อจัดกลุ่มข้อมูลใน scrabble ให้เป็น tuple แต่ละตัว โดยแต่ละกลุ่มจะอยู่ในรูป [ตัวอักษร, คะแนน, จำนวน, สัดส่วน] 
# จากนั้นแปลง zip เป็น list ทำให้ data เก็บรายการข้อมูลในรูปแบบที่ใช้งานได้ง่าย เช่น [('a', 1, 9, 4.8), ('b', 3, 2, 3.2), ...]

# ข้อ 1: แสดงตัวอักษรที่มีคะแนนสูงสุด 4 อันดับแรกพร้อมคะแนน
top_points = sorted(data, key=lambda x: x[1], reverse=True)[:4]
top_points_output = list(map(lambda x: f'"{x[0]}" with {x[1]} points.', top_points))
# เรียงลำดับ data ตามคะแนน (x[1]) จากมากไปน้อยและเลือกเฉพาะ 4 อันดับแรก
# ใช้ map เพื่อจัดข้อความในรูปแบบ "<ตัวอักษร>" with <คะแนน> points.

# ข้อ 2: แสดงตัวอักษรที่มีจำนวนมากที่สุด 4 อันดับแรกพร้อมจำนวน
top_amounts = sorted(data, key=lambda x: x[2], reverse=True)[:4] 
top_amounts_output = list(map(lambda x: f'"{x[0]}" with {x[2]} pieces.', top_amounts))
# เรียงลำดับ data ตามจำนวน (x[2]) จากมากไปน้อยและเลือกเฉพาะ 4 อันดับแรก
# ใช้ map เพื่อจัดข้อความในรูปแบบ "<ตัวอักษร>" with <จำนวน> pieces.

# ข้อ 3: แสดงตัวอักษรที่มีสัดส่วนต่ำสุด 4 อันดับแรกพร้อมสัดส่วน
low_ratios = sorted(data, key=lambda x: x[3])[:4]
low_ratios_output = list(map(lambda x: f'"{x[0]}" with {x[3]} percent.', low_ratios))
# เรียงลำดับ data ตามสัดส่วน (x[3]) จากน้อยไปมากและเลือกเฉพาะ 4 อันดับแรก
# ใช้ map เพื่อจัดข้อความในรูปแบบ "<ตัวอักษร>" with <สัดส่วน> percent.

# ฟังก์ชันเพื่อจัดรูปแบบการแสดงผลที่มีเลขลำดับและจัดตรงกลาง
def format_output(title, items):
    max_width = max(len(title), max(len(f"{i+1}) {item}") for i, item in enumerate(items)))
    centered_title = title.center(max_width)
    centered_items = "\n".join([f"{i+1}) {item}".center(max_width) for i, item in enumerate(items)])
    return f"{centered_title}\n{centered_items}"
# ฟังก์ชันนี้รับ title (หัวข้อการแสดงผล) และ items (รายการข้อมูลที่ต้องการแสดง) มาจัดรูปแบบการแสดงผลให้อยู่ตรงกลาง
# คำนวณความกว้าง (max_width) ให้พอดีที่สุดสำหรับข้อความ
# สร้างข้อความที่มีเลขลำดับหน้ารายการ และจัดให้อยู่ตรงกลาง (center

# แสดงผลลัพธ์พร้อมเลขข้อและลำดับ
print(format_output("The highest point in the scrabble game: ", top_points_output))
print(format_output("The highest amount in the scrabble game:", top_amounts_output))
print(format_output("The lowest ratio in the scrabble game:", low_ratios_output))
