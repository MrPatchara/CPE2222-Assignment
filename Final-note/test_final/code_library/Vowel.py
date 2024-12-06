# โปรแกรมรับข้อความจากผู้ใช้และลบตัวอักษรที่เป็นสระออกจากข้อความนั้น
input_text = str(input())

vowels = "aeiouAEIOU"

remove = ''.join(char for char in input_text if char not in vowels)

print(remove)