# โปรแกรมตัวอย่างการใช้งาน JSON ใน Python
import json

def read_json_file(filename):
    # อ่านข้อมูลจากไฟล์ JSON
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"ไม่พบไฟล์ {filename}")
        return None

# ตัวอย่างการใช้งาน
filename = "example.json"
data = {
    "ชื่อ": "เอิร์ธ",
    "อายุ": 25,
    "อาชีพ": "ผีบ้า"
}

# บันทึกข้อมูลตัวอย่างลงไฟล์ JSON
with open(filename, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

# อ่านข้อมูลจากไฟล์ JSON
loaded_data = read_json_file(filename)
if loaded_data:
    print("ข้อมูลในไฟล์ JSON:")
    print(loaded_data)
