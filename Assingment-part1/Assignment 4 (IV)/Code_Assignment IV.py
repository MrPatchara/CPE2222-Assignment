# Assignment IV: String Manipulation
# กำหนดตัวแปรสายอักขระ s1, s2, และ s3
s1 = "Python is a powerful high-level, object-oriented programming language created by Guido van Rossum."
s2 = "It has simple easy-to-use syntax, making it the perfect language for someone trying to learn computer programming for the first time."
s3 = "Professionally, Python is great for backend web development, data analysis, artificial intelligence, and scientific computing."
# s1, s2, และ s3 เป็นข้อความที่เกี่ยวกับ Python แต่ละบรรทัดเป็นข้อมูลเกี่ยวกับจุดเด่นและการใช้งานของภาษา Python

# หาจำนวนตัวอักษรทั้งหมด (total_characters)
total_characters = len(s1) + len(s2) + len(s3) # หาจำนวนตัวอักษรทั้งหมด
print("Total characters in string s1, s2 and s3 are", total_characters ,"characters") 
# ใช้ฟังก์ชัน len() เพื่อหาความยาวของแต่ละข้อความ (s1, s2, และ s3) ซึ่งแสดงถึงจำนวนตัวอักษรในแต่ละสายอักขระ
# นำผลลัพธ์จาก len() ของแต่ละข้อความมาบวกกันเพื่อหาจำนวนตัวอักษรรวมทั้งหมด และแสดงผลลัพธ์

# หาจำนวนคำทั้งหมด (total_words)
total_words = len(s1.split()) + len(s2.split()) + len(s3.split()) # หาจำนวนคำทั้งหมดด้วยการใช้ split()
print("Total words in string s1, s2 and s3 are", total_words, "words")
# ใช้ฟังก์ชัน split() แยกคำในแต่ละสายอักขระที่คั่นด้วยช่องว่าง (" ") ซึ่งจะได้รายการของคำแต่ละคำในสายอักขระนั้น
# นำรายการคำที่ได้ไปใช้กับฟังก์ชัน len() เพื่อหาจำนวนคำ จากนั้นนำจำนวนคำใน s1, s2, และ s3 มาบวกกันเพื่อหาจำนวนคำรวมทั้งหมด และแสดงผลลัพธ์

# ค้นหารหัสลับจาก s1 (hidden_code_s1)
hidden_code_s1 = s1[-20] + s1[-3] + s1[-81] # หารหัสลับจากตัวอักษรที่กำหนด
# เลือกตัวอักษรจาก s1 ที่ตำแหน่งที่ระบุ:
# s1[-20]: ตัวอักษรที่ตำแหน่ง -20 จากท้ายข้อความ
# s1[-3]: ตัวอักษรที่ตำแหน่ง -3 จากท้ายข้อความ
# s1[-81]: ตัวอักษรที่ตำแหน่ง -81 จากท้ายข้อความ
# นำตัวอักษรที่ได้มารวมกันในตัวแปร hidden_code_s1

# ค้นหารหัสลับจาก s2 (hidden_code_s2)
s2_no_spaces = s2.replace(" ", "")# ลบช่องว่างออกจากสายอักขระ
hidden_code_s2 = s2_no_spaces[43] + s2_no_spaces[3] # หารหัสลับจากตำแหน่งที่กำหนด
# ใช้ replace(" ", "") ลบช่องว่างออกจาก s2 ทำให้ข้อความ s2_no_spaces ไม่มีช่องว่าง
# เลือกตัวอักษรจาก s2_no_spaces ที่ตำแหน่งที่ระบุ:
# s2_no_spaces[43]: ตัวอักษรที่ตำแหน่ง 43
# s2_no_spaces[3]: ตัวอักษรที่ตำแหน่ง 3

# ค้นหารหัสลับจาก s3 (hidden_code_s3)
s3_no_spaces = s3.replace(" ", "")
hidden_code_s3 = s3_no_spaces[-31] + s3_no_spaces[-9] 
# ใช้ replace(" ", "") ลบช่องว่างออกจาก s3 ทำให้ข้อความ s3_no_spaces ไม่มีช่องว่าง
# เลือกตัวอักษรจาก s3_no_spaces ที่ตำแหน่งที่ระบุ:
# s3_no_spaces[-31]: ตัวอักษรที่ตำแหน่ง -31 จากท้ายข้อความ
# s3_no_spaces[-9]: ตัวอักษรที่ตำแหน่ง -9 จากท้ายข้อความ

# แสดงรหัสลับเรียงต่อกัน
hidden_code = hidden_code_s1 + hidden_code_s2 + hidden_code_s3
print("The secret code is:", hidden_code)


