import os
import shutil

# ฟังก์ชันอ่านข้อมูลจากไฟล์และจัดกลุ่มข้อมูลตามประเภทบุคคลและสาขาวิชา
def read_and_categorize_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = {
        'นักศึกษา': [],
        'อาจารย์': {
            'วิศวกรรมโยธา': [],
            'วิศวกรรมอุตสาหการ': [],
            'วิศวกรรมคอมพิวเตอร์': []
        }
    }

    current_person = []
    for line in lines:
        # หากเจอบรรทัดว่าง ให้ถือว่าจบข้อมูลของคนๆ หนึ่ง
        if line.strip() == '':
            if current_person:
                # ตรวจสอบประเภทและสาขาวิชา
                if 'สถานะ: นักศึกษา' in current_person:
                    data['นักศึกษา'].append(current_person)
                elif 'ตำแหน่ง: อาจารย์' in current_person:
                    for branch in data['อาจารย์']:
                        if f'สาขาวิชา: {branch}' in current_person:
                            data['อาจารย์'][branch].append(current_person)
                            break
                current_person = []
        else:
            current_person.append(line.strip())
    
    # ตรวจสอบข้อมูลคนสุดท้ายหากไม่สิ้นสุดด้วยบรรทัดว่าง
    if current_person:
        if 'สถานะ: นักศึกษา' in current_person:
            data['นักศึกษา'].append(current_person)
        elif 'ตำแหน่ง: อาจารย์' in current_person:
            for branch in data['อาจารย์']:
                if f'สาขาวิชา: {branch}' in current_person:
                    data['อาจารย์'][branch].append(current_person)
                    break

    return data

# ฟังก์ชันสร้างโครงสร้าง Directory และบันทึกข้อมูลลงในไฟล์ readme.txt และรายชื่อพนักงานและนักศึกษา
def create_directory_structure(data, readme_source):
    base_dir = 'รายชื่อ'
    os.makedirs(base_dir, exist_ok=True)
    
    # สร้างไฟล์ readme.txt หลักในโฟลเดอร์ 'รายชื่อ'
    shutil.copy(readme_source, os.path.join(base_dir, 'readme.txt'))
    
    # สร้างไฟล์รายชื่อพนักงานและนักศึกษา.txt ในโฟลเดอร์ 'รายชื่อ'
    with open(os.path.join(base_dir, 'รายชื่อพนักงานและนักศึกษา.txt'), 'w', encoding='utf-8') as f:
        f.write("รายชื่อพนักงานและนักศึกษา\n")
        index = 1
        for student in data['นักศึกษา']:
            name = student[0]  # บรรทัดแรกคือชื่อ
            f.write(f"{index}. {name}\n")
            index += 1
        for branch, teachers in data['อาจารย์'].items():
            for teacher in teachers:
                name = teacher[0]  # บรรทัดแรกคือชื่อ
                f.write(f"{index}. {name}\n")
                index += 1

    # สร้างโฟลเดอร์ นักศึกษา และไฟล์ที่เกี่ยวข้อง
    student_dir = os.path.join(base_dir, 'นักศึกษา')
    os.makedirs(student_dir, exist_ok=True)
    shutil.copy(readme_source, os.path.join(student_dir, 'readme.txt'))
    with open(os.path.join(student_dir, 'รายชื่อนักศึกษาคณะวิศวกรรมศาสตร์.txt'), 'w', encoding='utf-8') as f:
        f.write("รายชื่อนักศึกษาคณะวิศวกรรมศาสตร์\n")
        for i, student in enumerate(data['นักศึกษา'], 1):
            name = student[0]  # บรรทัดแรกคือชื่อ
            f.write(f"{i}. {name}\n")

    # สร้างโฟลเดอร์ อาจารย์ และไฟล์ที่เกี่ยวข้อง
    teacher_dir = os.path.join(base_dir, 'อาจารย์')
    os.makedirs(teacher_dir, exist_ok=True)
    shutil.copy(readme_source, os.path.join(teacher_dir, 'readme.txt'))
    with open(os.path.join(teacher_dir, 'รายชื่ออาจารย์คณะวิศวกรรมศาสตร์.txt'), 'w', encoding='utf-8') as f:
        f.write("รายชื่ออาจารย์คณะวิศวกรรมศาสตร์\n")
        index = 1
        for branch, teachers in data['อาจารย์'].items():
            for teacher in teachers:
                name = teacher[0]  # บรรทัดแรกคือชื่อ
                f.write(f"{index}. {name}\n")
                index += 1

    # สร้างโฟลเดอร์สำหรับแต่ละสาขาวิชาของอาจารย์
    for branch, teachers in data['อาจารย์'].items():
        branch_dir = os.path.join(teacher_dir, branch.replace('วิศวกรรม', 'วิศวกรรม'))
        os.makedirs(branch_dir, exist_ok=True)
        shutil.copy(readme_source, os.path.join(branch_dir, 'readme.txt'))
        with open(os.path.join(branch_dir, f'รายชื่ออาจารย์สาขา{branch.replace("วิศวกรรม", "")}.txt'), 'w', encoding='utf-8') as f:
            f.write(f"รายชื่ออาจารย์สาขา{branch.replace('วิศวกรรม', '')}\n")
            for i, teacher in enumerate(teachers, 1):
                name = teacher[0]  # บรรทัดแรกคือชื่อ
                f.write(f"{i}. {name}\n")

# Path ของไฟล์ input และ readme template
input_file = 'input.txt'
readme_file = 'readme.txt'  # กำหนดชื่อไฟล์ readme ที่จะใช้ copy

# อ่านข้อมูลและจัดกลุ่ม
data = read_and_categorize_data(input_file)

# สร้างโครงสร้าง Directory และบันทึกข้อมูล
create_directory_structure(data, readme_file)

print("Directory structure created and data categorized successfully!")
