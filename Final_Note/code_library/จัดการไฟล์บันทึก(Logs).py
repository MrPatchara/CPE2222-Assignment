#โปรแกรมอ่านและวิเคราะห์ไฟล์บันทึก (Log File) เพื่อหาข้อความสำคัญ
def search_logs(filename, keyword):
    # ค้นหาคำสำคัญในไฟล์บันทึก
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            matches = [line.strip() for line in lines if keyword in line]
            return matches
    except FileNotFoundError:
        print(f"ไม่พบไฟล์: {filename}")
        return []

# ตัวอย่างการใช้งาน
filename = "server_logs.txt"  # เปลี่ยนชื่อไฟล์ตามต้องการ
keyword = input("กรุณาใส่คำสำคัญที่ต้องการค้นหาใน Log File: ")
results = search_logs(filename, keyword)
if results:
    print(f"พบข้อความที่ตรงกับคำสำคัญ '{keyword}':")
    for line in results:
        print(line)
else:
    print(f"ไม่พบข้อความที่ตรงกับคำสำคัญ '{keyword}'")