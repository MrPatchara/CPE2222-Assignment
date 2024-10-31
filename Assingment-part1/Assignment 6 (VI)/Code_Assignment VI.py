# Assignment VI: Nested Dictionaries
# สร้างพจนานุกรมซ้อนพจนานุกรม
student_data = {
    'Peter': {'Age': 40,'Gender': 'Male','Test': {'First': 20,'Second': 18,'Third': 19}},
    'Paul': {'Age': 25,'Gender': 'Male','Test': {'First': 19,'Second': 20,'Third': 19}},
    'Mary': {'Age': 18,'Gender': 'Female','Test': {'First': 10,'Second': 5,'Third': 4}},
    'Jenny': {'Age': 60,'Gender': 'Female','Test': {'First': 5,'Second': 3,'Third': 1}}
}
# student_data เป็นพจนานุกรมหลัก โดยใช้ชื่อนักเรียนเป็นคีย์ ('Peter', 'Paul', 'Mary', และ 'Jenny') โดยแต่ละคีย์มีค่าที่เป็นพจนานุกรมย่อย
# แต่ละพจนานุกรมย่อยของนักเรียนจะเก็บข้อมูล Age (อายุ), Gender (เพศ) และ Test ซึ่งเป็นพจนานุกรมย่อยอีกชุดหนึ่งสำหรับเก็บคะแนนสอบ (First, Second, Third)

# 1) แสดงเพศ (Gender) ของ Peter
print('"Peter" is', student_data['Peter']['Gender'])
# ดึงข้อมูล Gender ของ Peter โดยระบุคีย์ 'Peter' จากนั้นเข้าถึงข้อมูลเพศด้วยคีย์ 'Gender'
# ผลลัพธ์: "Peter" is Male

# 2) แสดงผลสอบ (Test) ครั้งที่ 1 (First) ของ Mary
print('The 1st test score of "Mary" is', student_data['Mary']['Test']['First'])
# เข้าถึงคีย์ 'Mary' จากนั้นไปที่คีย์ 'Test' ซึ่งเป็นพจนานุกรมเก็บคะแนนสอบ และใช้คีย์ 'First' เพื่อดึงคะแนนสอบครั้งที่ 1
# ผลลัพธ์: The 1st test score of "Mary" is 10

# 3) แสดงผลสอบ (Test) ครั้งที่ 2 (Second) ของ Jenny
print('The 2st test score of "Jenny" is', student_data['Jenny']['Test']['Second'])
# เข้าถึงคีย์ 'Jenny' ไปยัง 'Test' และใช้คีย์ 'Second' เพื่อดึงคะแนนสอบครั้งที่ 2
# ผลลัพธ์: The 2st test score of "Jenny" is 3

# 4) แสดงผลสอบ (Test) ครั้งที่ 3 (Third) ของ Paul
print('The 3st test score of "Paul" is', student_data['Paul']['Test']['Third'])

# 5) เขียนคำสั่งในการเพิ่มข้อมูลลงในพจนานุกรม
student_data['Robert'] = {
    'Age': 35,'Gender': 'Male','Test': {'First': 10,'Second': 18,'Third': 5}
}

# 6) แสดงอายุ (Age) ของ Robert
print('"Robert" is', student_data['Robert']['Age'], 'years old')

# 7) แสดงโครงสร้างของพจนานุกรมที่นักศึกษาออกแบบ
print("The dictionary to solve this problem was designed as:")
print(student_data)
