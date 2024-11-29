import csv

def write_to_csv(filename, data):
    # เขียนข้อมูลลงไฟล์ CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ชื่อ", "อายุ", "อีเมล"])
        writer.writerows(data)
    print(f"บันทึกข้อมูลลงไฟล์ {filename} เรียบร้อย")

def read_from_csv(filename):
    # อ่านข้อมูลจากไฟล์ CSV
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"ไม่พบไฟล์ {filename}")

# ตัวอย่างการใช้งาน
filename = "data.csv"
data = [
    ["สมชาย", 25, "somchai@example.com"],
    ["สมหญิง", 30, "somying@example.com"]
]
write_to_csv(filename, data)
print("ข้อมูลในไฟล์:")
read_from_csv(filename)
