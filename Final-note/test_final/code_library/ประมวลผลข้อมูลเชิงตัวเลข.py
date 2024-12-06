# โปรแกรมคำนวณคะแนนข้อความด้วย ASCII
# คำนวณคะแนนของข้อความแต่ละตัวโดยใช้ค่า ASCII ของตัวอักษร
# ฟังก์ชันคำนวณคะแนนข้อความ
s1 = "madam and her racecar were at the radar station."
s2 = "They found a civic parked next to a kayak."
s3 = "Wow, what a day!"
    
def calculate_ascii_score(text):
    #คำนวณคะแนนจาก ASCII
    #- text: ข้อความที่ต้องการคำนวณ
    return sum(ord(char) for char in text if char.isalpha())

# คำนวณคะแนนสำหรับ s1, s2, s3
score_s1 = calculate_ascii_score(s1)
score_s2 = calculate_ascii_score(s2)
score_s3 = calculate_ascii_score(s3)

print(f"ASCII Score for s1: {score_s1}")
print(f"ASCII Score for s2: {score_s2}")
print(f"ASCII Score for s3: {score_s3}")
print(f"Total ASCII Score: {score_s1 + score_s2 + score_s3}")