# สร้างตัวแปร scrabble
scrabble = [
    'a', 1, 9, 4.8, 'b', 3, 2, 3.2, 'c', 3, 2, 3.2, 'd', 2, 4, 4.3, 'e', 1, 12, 6.4,
    'f', 4, 2, 4.3, 'g', 2, 3, 3.2, 'h', 4, 2, 4.3, 'i', 1, 9, 4.8, 'j', 8, 1, 4.3,
    'k', 5, 1, 2.7, 'l', 1, 4, 2.1, 'm', 3, 2, 3.2, 'n', 1, 6, 3.2, 'o', 1, 8, 4.3,
    'p', 3, 2, 3.2, 'q', 10, 1, 5.3, 'r', 1, 6, 3.2, 's', 1, 4, 2.1, 't', 1, 6, 3.2,
    'u', 1, 4, 2.1, 'v', 4, 2, 4.3, 'w', 4, 2, 4.3, 'x', 8, 1, 4.3, 'y', 4, 2, 4.3,
    'z', 10, 1, 5.3
]

# สร้างพจนานุกรม scrabble_dict
scrabble_dict = {}
for i in range(0, len(scrabble), 4):
    letter = scrabble[i]
    point = scrabble[i+1]
    amount = scrabble[i+2]
    scrabble_dict[letter] = {'score': point, 'amount': amount}

# แสดงผลพจนานุกรม
print("1) Scrabble List-to-Dictionary Conversion:")
print("--------------------------------------------------------------")
print(scrabble_dict)
print("==============================================================\n")

# รับคำจากผู้ใช้
print("2) Score of your word")
print("--------------------------------------------------------------")
word = input("Enter Your Word [Only alphabets]: ").strip().lower()

# ตรวจสอบว่าเป็นตัวอักษรภาษาอังกฤษเท่านั้น
if not word.isalpha():
    print("Invalid input. Please enter only letters.")
else:
    # คำนวณคะแนนรวม
    total_score = 0
    temp_dict = scrabble_dict.copy()  # สำเนาพจนานุกรมเพื่อลดจำนวนตัวอักษรในกรณีที่ถูกใช้
    valid = True

    # ตรวจสอบและคำนวณคะแนน
    for char in word:
        if char in temp_dict and temp_dict[char]['amount'] > 0:
            total_score += temp_dict[char]['score']
            temp_dict[char]['amount'] -= 1
        else:
            valid = False
            break

    if valid:
        print(f"Total score of \"{word}\" is {total_score}")

        # ปรับปรุงพจนานุกรมให้เหลือเฉพาะตัวอักษรที่ใช้ในคำที่ป้อน
        print("\n3) Updated Scrabble Dictionary")
        print("--------------------------------------------------------------")

        # สร้างพจนานุกรมที่อัปเดต โดยหักจำนวนที่ใช้จากคำ
        updated_dict = {}
        for char in set(word):  # ใช้ set เพื่อไม่ให้ตัวอักษรซ้ำ
            if char in scrabble_dict:
                used_count = word.count(char)  # จำนวนที่ใช้ในคำ
                updated_dict[char] = {
                    'score': scrabble_dict[char]['score'],
                    'amount': scrabble_dict[char]['amount'] - used_count  # หักจำนวนที่ใช้
                }

        # เรียงลำดับพจนานุกรมตามตัวอักษร
        sorted_updated_dict = dict(sorted(updated_dict.items()))

        print(sorted_updated_dict)
    else:
        print(f"The word \"{word}\" cannot be formed due to insufficient letters.")
