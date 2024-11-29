#วิเคราะห์ความถี่ของตัวอักษรที่ปรากฏใน s1, s2, s3 และสร้างกราฟแท่ง (Bar Chart)
import matplotlib.pyplot as plt
from collections import Counter

# รวมข้อความทั้งหมด
combined_text = s1 + s2 + s3

# นับความถี่ของตัวอักษร (เฉพาะ a-z หรือ A-Z)
letter_frequency = Counter(char.lower() for char in combined_text if char.isalpha())

# แสดงผลความถี่ตัวอักษร
print("Letter Frequency:")
for letter, freq in letter_frequency.items():
    print(f"{letter}: {freq}")

# วาดกราฟแท่งแสดงความถี่ตัวอักษร
plt.bar(letter_frequency.keys(), letter_frequency.values(), color='skyblue')
plt.title("Letter Frequency in Text")
plt.xlabel("Letters")
plt.ylabel("Frequency")
plt.show()
