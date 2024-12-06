# โปรแกรมหาจำนวนตัวอักษร และจำนวนคำ และหา secret code จาก string ที่กำหนดให้
s1 = "Python is a powerful high-level, object-oriented programming language created by Guido van Rossum."
s2 = "It has simple easy-to-use syntax, making it the perfect language for someone trying to learn computer programming for the first time."
s3 = "Professionally, Python is great for backend web development, data analysis, artificial intelligence, and scientific computing."

#characters
total_char = len(s1) + len(s2) + len(s3)
print(f"Total characters in string s1, s2 and s3 are {total_char} characters")

#words
total_split = s1.split() + s2.split() + s3.split()
total_word = len(total_split)
print(f"Total words in string s1, s2 and s3 are {total_word} words")

#secret
s1_secret = s1[::-1][19] + s1[::-1][2] + s1[::-1][80]

s2_no_space = s2.replace(" ", "")
s2_secret = s2_no_space[43] + s2_no_space[3]

s3_no_space = s3.replace(" ","")
s3_secret = s3_no_space[::-1][30] + s3_no_space[::-1][8]

secret_code = s1_secret + s2_secret + s3_secret

print(f"The secret code is {secret_code}")