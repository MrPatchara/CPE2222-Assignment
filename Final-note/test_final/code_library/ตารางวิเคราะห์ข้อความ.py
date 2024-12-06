# โปรแกรมวิเคราะห์ข้อความ โดยนับจำนวนตัวอักษรทั้งหมด, คำทั้งหมด, และคำที่ไม่ซ้ำกัน
# สร้างตารางวิเคราะห์ข้อความในรูปแบบของตัวอักษรทั้งหมด, คำทั้งหมด, และตัวเลขคำเฉพาะ
# สร้างข้อมูลการวิเคราะห์
s1 = "madam and her racecar were at the radar station."
s2 = "They found a civic parked next to a kayak."
s3 = "Wow, what a day!"

analysis = {
    "String": ["s1", "s2", "s3"],
    "Total Characters": [len(s1), len(s2), len(s3)],
    "Total Words": [len(s1.split()), len(s2.split()), len(s3.split())],
    "Unique Words": [len(set(s1.split())), len(set(s2.split())), len(set(s3.split()))],
}

# แสดงผลการวิเคราะห์ในรูปแบบตาราง
print(f"{'String':<10}{'Total Characters':<20}{'Total Words':<15}{'Unique Words':<15}")
print("-" * 60)
for i in range(3):
    print(f"{analysis['String'][i]:<10}{analysis['Total Characters'][i]:<20}{analysis['Total Words'][i]:<15}{analysis['Unique Words'][i]:<15}")
