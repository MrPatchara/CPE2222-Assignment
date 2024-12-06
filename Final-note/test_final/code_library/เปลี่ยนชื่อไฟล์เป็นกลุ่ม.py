#โปรแกรมเปลี่ยนชื่อไฟล์ในโฟลเดอร์ทั้งหมดด้วยชื่อที่กำหนด
import os

def batch_rename_files(folder, new_name, extension):
    try:
        files = os.listdir(folder)
        for i, file in enumerate(files):
            old_path = os.path.join(folder, file)
            new_path = os.path.join(folder, f"{new_name}_{i + 1}.{extension}")
            os.rename(old_path, new_path)
        print("เปลี่ยนชื่อไฟล์สำเร็จ")
    except FileNotFoundError:
        print(f"ไม่พบโฟลเดอร์ {folder}")

# ตัวอย่างการใช้งาน
folder = "example_folder"
new_name = "renamed_file"
extension = "txt"
batch_rename_files(folder, new_name, extension)