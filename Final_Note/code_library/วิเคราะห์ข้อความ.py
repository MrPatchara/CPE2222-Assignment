#โปรแกรมนับจำนวนคำ ตัวอักษร และวิเคราะห์ข้อความอื่น ๆ
def analyze_text(text):
    num_characters = len(text)
    num_words = len(text.split())
    num_lines = len(text.splitlines())
    return num_characters, num_words, num_lines

# รับข้อมูลจากผู้ใช้
text = input("กรุณาใส่ข้อความที่ต้องการวิเคราะห์: ")

# วิเคราะห์ข้อความ
characters, words, lines = analyze_text(text)
print(f"จำนวนตัวอักษร: {characters}")
print(f"จำนวนคำ: {words}")
print(f"จำนวนบรรทัด: {lines}")