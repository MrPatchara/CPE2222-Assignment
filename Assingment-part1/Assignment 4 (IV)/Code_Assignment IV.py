# Assignment IV: String Manipulation
# กำหนดตัวแปรสายอักขระ s1, s2, และ s3
s1 = "Python is a powerful high-level, object-oriented programming language created by Guido van Rossum."
s2 = "It has simple easy-to-use syntax, making it the perfect language for someone trying to learn computer programming for the first time."
s3 = "Professionally, Python is great for backend web development, data analysis, artificial intelligence, and scientific computing."


# หาจำนวนตัวอักษรทั้งหมด (total_characters)
total_characters = len(s1) + len(s2) + len(s3) # หาจำนวนตัวอักษรทั้งหมด
print("Total characters in string s1, s2 and s3 are", total_characters ,"characters") 


# หาจำนวนคำทั้งหมด (total_words)
total_words = len(s1.split()) + len(s2.split()) + len(s3.split()) 
print("Total words in string s1, s2 and s3 are", total_words, "words")

# ค้นหารหัสลับจาก s1 (hidden_code_s1)
hidden_code_s1 = s1[-20] + s1[-3] + s1[-81] 

# ค้นหารหัสลับจาก s2 (hidden_code_s2)
s2_no_spaces = s2.replace(" ", "")# ลบช่องว่างออกจากสายอักขระ
hidden_code_s2 = s2_no_spaces[43] + s2_no_spaces[3] # หารหัสลับจากตำแหน่งที่กำหนด

# ค้นหารหัสลับจาก s3 (hidden_code_s3)
s3_no_spaces = s3.replace(" ", "")
hidden_code_s3 = s3_no_spaces[-31] + s3_no_spaces[-9] 

hidden_code = hidden_code_s1 + hidden_code_s2 + hidden_code_s3
print("The secret code is:", hidden_code)


