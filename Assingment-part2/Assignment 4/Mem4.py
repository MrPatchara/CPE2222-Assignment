import os # นำเข้าโมดูล os สำหรับการจัดการไฟล์และโฟลเดอร์
import shutil # นำเข้าโมดูล shutil สำหรับการคัดลอกไฟล์และโฟลเดอร์

# ฟังก์ชันอ่านข้อมูลจากไฟล์และจัดกลุ่มข้อมูลตามประเภทบุคคลและสาขาวิชา
def read_and_categorize_data(filename): # รับพารามิเตอร์เป็นชื่อไฟล์ที่ต้องการอ่านข้อมูล
    with open(filename, 'r', encoding='utf-8') as f: # เปิดไฟล์ที่ต้องการอ่านข้อมูล โดยใช้ utf-8 เพื่ออ่านภาษาไทย 
        lines = f.readlines() # อ่านข้อมูลทั้งหมดจากไฟล์และเก็บไว้ในตัวแปร lines

    data = {
        'นักศึกษา': [], # สร้าง list เปล่าสำหรับเก็บข้อมูลนักศึกษา
        'อาจารย์': {
            'วิศวกรรมโยธา': [],
            'วิศวกรรมอุตสาหการ': [],
            'วิศวกรรมคอมพิวเตอร์': []
        } # สร้าง dict เปล่าสำหรับเก็บข้อมูลอาจารย์แยกตามสาขาวิชา
    }

    current_person = [] # สร้าง list เปล่าสำหรับเก็บข้อมูลบุคคลคนปัจจุบัน
    for line in lines:  # วนลูปอ่านข้อมูลทีละบรรทัด
        # หากเจอบรรทัดว่าง ให้ถือว่าจบข้อมูลของคนๆ หนึ่ง
        if line.strip() == '': # ตรวจสอบว่าบรรทัดเป็นว่างหรือไม่
            if current_person: 
                # ตรวจสอบประเภทและสาขาวิชา
                if 'สถานะ: นักศึกษา' in current_person: # ตรวจสอบว่าเป็นนักศึกษาหรือไม่
                    data['นักศึกษา'].append(current_person) # เพิ่มข้อมูลนักศึกษาลงใน list ของนักศึกษา
                elif 'ตำแหน่ง: อาจารย์' in current_person: # ตรวจสอบว่าเป็นอาจารย์หรือไม่
                    for branch in data['อาจารย์']: # วนลูปเพื่อตรวจสอบสาขาวิชาของอาจารย์
                        if f'สาขาวิชา: {branch}' in current_person: # ตรวจสอบว่าอาจารย์สาขาวิชานี้หรือไม่
                            data['อาจารย์'][branch].append(current_person) # เพิ่มข้อมูลอาจารย์ลงใน list ของอาจารย์สาขานั้น
                            break
                current_person = [] # ล้างข้อมูลบุคคลปัจจุบันเพื่อเตรียมรับข้อมูลคนใหม่
        else: # หากไม่ใช่บรรทัดว่าง
            current_person.append(line.strip()) # เพิ่มข้อมูลบุคคลปัจจุบันด้วยการลบช่องว่างด้านหน้าและหลังข้อความ
    
    # ตรวจสอบข้อมูลคนสุดท้ายหากไม่สิ้นสุดด้วยบรรทัดว่าง
    if current_person:
        if 'สถานะ: นักศึกษา' in current_person: # ตรวจสอบว่าเป็นนักศึกษาหรือไม่
            data['นักศึกษา'].append(current_person) # เพิ่มข้อมูลนักศึกษาลงใน list ของนักศึกษา
        elif 'ตำแหน่ง: อาจารย์' in current_person: # ตรวจสอบว่าเป็นอาจารย์หรือไม่
            for branch in data['อาจารย์']: # วนลูปเพื่อตรวจสอบสาขาวิชาของอาจารย์
                if f'สาขาวิชา: {branch}' in current_person: # ตรวจสอบว่าอาจารย์สาขาวิชานี้หรือไม่
                    data['อาจารย์'][branch].append(current_person) # เพิ่มข้อมูลอาจารย์ลงใน list ของอาจารย์สาขานั้น
                    break

    return data

# ฟังก์ชันสร้างโครงสร้าง Directory และบันทึกข้อมูลลงในไฟล์ readme.txt และรายชื่อพนักงานและนักศึกษา
def create_directory_structure(data, readme_source): # รับพารามิเตอร์เป็นข้อมูลที่จัดกลุ่มและไฟล์ readme ที่จะใช้ copy
    base_dir = 'รายชื่อ' # กำหนดชื่อโฟลเดอร์หลัก
    os.makedirs(base_dir, exist_ok=True) # สร้างโฟลเดอร์หลัก หากยังไม่มี
    
    # สร้างไฟล์ readme.txt หลักในโฟลเดอร์ 'รายชื่อ'
    shutil.copy(readme_source, os.path.join(base_dir, 'readme.txt')) # คัดลอกไฟล์ readme ที่จะใช้ copy ไปยังโฟลเดอร์ 'รายชื่อ'
    
    # สร้างไฟล์รายชื่อพนักงานและนักศึกษา.txt ในโฟลเดอร์ 'รายชื่อ'
    with open(os.path.join(base_dir, 'รายชื่อพนักงานและนักศึกษา.txt'), 'w', encoding='utf-8') as f:
        f.write("รายชื่อพนักงานและนักศึกษา\n") # เขียนข้อความบรรทัดแรกของไฟล์
        index = 1
        for student in data['นักศึกษา']: # วนลูปเพื่อเขียนรายชื่อนักศึกษา
            name = student[0]  # บรรทัดแรกคือชื่อ
            f.write(f"{index}. {name}\n") # เขียนรายชื่อนักศึกษา
            index += 1 
        for branch, teachers in data['อาจารย์'].items(): # วนลูปเพื่อเขียนรายชื่ออาจารย์
            for teacher in teachers:
                name = teacher[0]  # บรรทัดแรกคือชื่อ
                f.write(f"{index}. {name}\n")
                index += 1

    # สร้างโฟลเดอร์ นักศึกษา และไฟล์ที่เกี่ยวข้อง
    student_dir = os.path.join(base_dir, 'นักศึกษา')
    os.makedirs(student_dir, exist_ok=True) 
    shutil.copy(readme_source, os.path.join(student_dir, 'readme.txt')) # คัดลอกไฟล์ readme ที่จะใช้ copy ไปยังโฟลเดอร์ 'นักศึกษา'
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
    for branch, teachers in data['อาจารย์'].items(): # วนลูปเพื่อสร้างโฟลเดอร์สำหรับแต่ละสาขาวิชาของอาจารย์
        branch_dir = os.path.join(teacher_dir, branch.replace('วิศวกรรม', 'วิศวกรรม'))  # สร้างชื่อโฟลเดอร์สำหรับสาขาวิชา 
        os.makedirs(branch_dir, exist_ok=True)
        shutil.copy(readme_source, os.path.join(branch_dir, 'readme.txt'))
        with open(os.path.join(branch_dir, f'รายชื่ออาจารย์สาขา{branch.replace("วิศวกรรม", "")}.txt'), 'w', encoding='utf-8') as f: # สร้างไฟล์รายชื่ออาจารย์สาขาวิชา
            f.write(f"รายชื่ออาจารย์สาขา{branch.replace('วิศวกรรม', '')}\n") 
            for i, teacher in enumerate(teachers, 1): # วนลูปเพื่อเขียนรายชื่ออาจารย์สาขาวิชา
                name = teacher[0]  # บรรทัดแรกคือชื่อ
                f.write(f"{i}. {name}\n") # เขียนรายชื่ออาจารย์สาขาวิชา

# Path ของไฟล์ input และ readme template
input_file = 'input.txt'
readme_file = 'readme.txt'  # กำหนดชื่อไฟล์ readme ที่จะใช้ copy

# อ่านข้อมูลและจัดกลุ่ม
data = read_and_categorize_data(input_file)

# สร้างโครงสร้าง Directory และบันทึกข้อมูล
create_directory_structure(data, readme_file)

print("Directory structure created and data categorized successfully!")
