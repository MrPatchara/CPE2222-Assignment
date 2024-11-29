def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"ข้อความถูกบันทึกลงไฟล์ {filename}")


def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            print("เนื้อหาในไฟล์:")
            print(file.read())
    except FileNotFoundError:
        print(f"ไม่พบไฟล์ {filename}")

# ตัวอย่างการใช้งาน
filename = "example.txt"
content = input("ใส่ข้อความที่ต้องการบันทึก: ")
save_to_file(filename, content)
read_from_file(filename)
