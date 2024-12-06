# โปรแกรมตรวจสอบคำที่เป็น palindrome จากข้อความที่กำหนดให้
# ตรวจสอบคำที่อ่านจากหน้าไปหลังหรือหลังไปหน้าได้เหมือนกัน (Palindrome)
# รวมข้อความทั้งหมดและแยกเป็นคำ
s1 = "madam and her racecar were at the radar station."
s2 = "They found a civic parked next to a kayak."
s3 = "Wow, what a day!"

words = (s1 + " " + s2 + " " + s3).split()

# ตรวจสอบคำที่เป็น palindrome
palindromes = [word for word in words if word.lower() == word[::-1].lower()]
print(f"Palindromes found: {palindromes if palindromes else 'None'}")
