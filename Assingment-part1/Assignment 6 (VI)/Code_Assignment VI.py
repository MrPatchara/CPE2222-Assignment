# สร้างพจนานุกรมซ้อนพจนานุกรม
student_data = {
    'Peter': {'Age': 40,'Gender': 'Male','Test': {'First': 20,'Second': 18,'Third': 19}},
    'Paul': {'Age': 25,'Gender': 'Male','Test': {'First': 19,'Second': 20,'Third': 19}},
    'Mary': {'Age': 18,'Gender': 'Female','Test': {'First': 10,'Second': 5,'Third': 4}},
    'Jenny': {'Age': 60,'Gender': 'Female','Test': {'First': 5,'Second': 3,'Third': 1}}
}

# 1) แสดงเพศ (Gender) ของ Peter
print('"Peter" is', student_data['Peter']['Gender'])

# 2) แสดงผลสอบ (Test) ครั้งที่ 1 (First) ของ Mary
print('The 1st test score of "Mary" is', student_data['Mary']['Test']['First'])

# 3) แสดงผลสอบ (Test) ครั้งที่ 2 (Second) ของ Jenny
print('The 2st test score of "Jenny" is', student_data['Jenny']['Test']['Second'])

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
