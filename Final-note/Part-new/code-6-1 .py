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
    score = scrabble[i + 1]
    amount = scrabble[i + 2]
    scrabble_dict[letter] = {'score': score, 'amount': amount}

# แสดงผลพจนานุกรม
print("1) Scrabble List-to-Dictionary Conversion:")
print("--------------------------------------------------------------")
print(scrabble_dict)
print("==============================================================\n")

# รับคำจากผู้ใช้
print("2) Score of your word")
print("--------------------------------------------------------------")
word = input("Enter Your Word [Only alphabets]: ").strip().lower()

# ตรวจสอบคำที่ป้อนว่ามีแต่ตัวอักษรภาษาอังกฤษหรือไม่
if not word.isalpha():
    print("Invalid input. Please enter only letters.")
else:
    # คำนวณคะแนนรวมและอัปเดตจำนวนตัวอักษร
    total_score = 0
    used_letters = {}

    # ตรวจสอบและคำนวณคะแนนรวม พร้อมนับตัวอักษรที่ใช้ในคำ
    for char in word:
        if char in scrabble_dict:
            # ตรวจสอบว่าในพจนานุกรมมีตัวอักษรพอหรือไม่
            if scrabble_dict[char]['amount'] > 0:
                total_score += scrabble_dict[char]['score']
                # นับจำนวนตัวอักษรที่ใช้ในคำ
                if char in used_letters:
                    used_letters[char] += 1
                else:
                    used_letters[char] = 1
            else:
                print(f"The letter '{char}' is not available enough in the dictionary.")
                break
        else:
            print(f"The letter '{char}' is not in the dictionary.")
            break
    else:
        # ตรวจสอบว่าตัวอักษรที่ใช้ในคำเกินจำนวนที่มีในพจนานุกรมหรือไม่
        for char in used_letters:
            if used_letters[char] > scrabble_dict[char]['amount']:
                print(f"The letter '{char}' is used more times than it appears in the dictionary.")
                break
        else:
            print(f"\nTotal score of \"{word}\" is {total_score}\n")

            # ปรับปรุงพจนานุกรมให้เหลือเฉพาะตัวอักษรที่ใช้ในคำที่ป้อน
            print("\n3) Updated Scrabble Dictionary")
            print("--------------------------------------------------------------")
            updated_dict = {}

            # ปรับพจนานุกรมให้แสดงเฉพาะตัวอักษรที่ใช้ในคำ
            for char in used_letters:
                if char in scrabble_dict:
                    updated_dict[char] = {
                        'score': scrabble_dict[char]['score'],
                        'amount': scrabble_dict[char]['amount'] - used_letters[char]
                    }

            # เรียงลำดับตามตัวอักษร a-z
            sorted_updated_dict = dict(sorted(updated_dict.items()))

            # แสดง Scrabble Dictionary ที่อัปเดตแล้ว
            print("Updated Scrabble Dictionary:")
            print(sorted_updated_dict)
