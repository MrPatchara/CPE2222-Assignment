# โปรแกรมสร้างโครงสร้าง Directory และบันทึกข้อมูลจากไฟล์ input.txt
import os
import shutil

# ฟังก์ชันสำหรับสร้าง Directory พร้อมคัดลอก readme.txt
def create_dir_with_readme(path):
    os.makedirs(path, exist_ok=True)
    shutil.copy('readme.txt', path)  # คัดลอก readme.txt เข้า Directory

# สร้าง Directory หลักและโครงสร้างย่อย
main_dir = "รายชื่อ"
create_dir_with_readme(main_dir)

# สร้าง Directory นักศึกษา
student_dir = os.path.join(main_dir, "นักศึกษา")
create_dir_with_readme(student_dir)

# สร้างไฟล์ รายชื่อนักศึกษาคณะวิศวกรรมศาสตร์.txt
student_file = os.path.join(student_dir, "รายชื่อนักศึกษาคณะวิศวกรรมศาสตร์.txt")
with open(student_file, 'w', encoding='utf-8') as f:
    f.write("ข้อมูลรายชื่อนักศึกษาคณะวิศวกรรมศาสตร์\n")

# สร้าง Directory อาจารย์
teacher_dir = os.path.join(main_dir, "อาจารย์")
create_dir_with_readme(teacher_dir)

# สร้างไฟล์ รายชื่อคณาจารย์คณะวิศวกรรมศาสตร์.txt
teacher_file = os.path.join(teacher_dir, "รายชื่อคณาจารย์คณะวิศวกรรมศาสตร์.txt")
with open(teacher_file, 'w', encoding='utf-8') as f:
    f.write("ข้อมูลรายชื่อคณาจารย์คณะวิศวกรรมศาสตร์\n")

# สร้าง Directory สาขาวิชาภายใน Directory อาจารย์
faculty_dirs = {
    "วิศวกรรมโยธา": os.path.join(teacher_dir, "วิศวกรรมโยธา"),
    "วิศวกรรมอุตสาหการ": os.path.join(teacher_dir, "วิศวกรรมอุตสาหการ"),
    "วิศวกรรมคอมพิวเตอร์": os.path.join(teacher_dir, "วิศวกรรมคอมพิวเตอร์"),
}

for faculty, path in faculty_dirs.items():
    create_dir_with_readme(path)
    # สร้างไฟล์รายชื่อสำหรับคณาจารย์ในแต่ละสาขา
    with open(os.path.join(path, f"รายชื่อคณาจารย์คณะ{faculty}.txt"), 'w', encoding='utf-8') as f:
        f.write(f"ข้อมูลรายชื่อคณาจารย์คณะ{faculty}\n")

# อ่านและจัดเก็บข้อมูลจาก input.txt
with open('input.txt', 'r', encoding='utf-8') as file:
    person_data = ""  # ข้อมูลชั่วคราวของบุคคลแต่ละคน
    person_type = None  # ใช้เก็บสถานะ นักศึกษา/อาจารย์
    faculty = None  # ใช้เก็บสาขาวิชา
    student_count = 1  # ตัวแปรสำหรับนับลำดับนักศึกษา
    teacher_count = 1  # ตัวแปรสำหรับนับลำดับอาจารย์
    faculty_counts = {faculty: 1 for faculty in faculty_dirs}  # ตัวแปรนับลำดับในแต่ละสาขาวิชา

    for line in file:
        line = line.strip()
        if not line:  # เจอบรรทัดว่าง ให้บันทึกข้อมูล
            if person_type == "นักศึกษา":
                # แยกชื่อจากข้อมูล
                name = person_data.split('\n')[0]  # ชื่อจะเป็นบรรทัดแรก
                with open(student_file, 'a', encoding='utf-8') as f:
                    f.write(f"{student_count}) {name}\n")  # แสดงหมายเลขลำดับและชื่อ
                student_count += 1  # เพิ่มหมายเลขลำดับนักศึกษา
            elif person_type == "อาจารย์":
                # แยกชื่อจากข้อมูล
                name = person_data.split('\n')[0]  # ชื่อจะเป็นบรรทัดแรก
                with open(teacher_file, 'a', encoding='utf-8') as f:
                    f.write(f"{teacher_count}) {name}\n")  # แสดงหมายเลขลำดับและชื่อ
                teacher_count += 1  # เพิ่มหมายเลขลำดับอาจารย์

                # บันทึกข้อมูลแยกตามสาขาวิชาในไฟล์สาขา
                if faculty in faculty_dirs:
                    faculty_file = os.path.join(faculty_dirs[faculty], f"รายชื่อคณาจารย์คณะ{faculty}.txt")
                    with open(faculty_file, 'a', encoding='utf-8') as f:
                        f.write(f"{faculty_counts[faculty]}) {name}\n")  # แสดงหมายเลขลำดับและชื่อ
                    faculty_counts[faculty] += 1  # เพิ่มหมายเลขลำดับในสาขาวิชา

            # เคลียร์ข้อมูลชั่วคราวเพื่อบันทึกคนถัดไป
            person_data = ""
            person_type = None
            faculty = None
        else:
            # สะสมข้อมูลของบุคคลแต่ละคน
            if line.startswith("สถานะ:") or line.startswith("ตำแหน่ง:"):
                person_type = line.split(": ")[1]
            elif line.startswith("สาขาวิชา:"):
                faculty = line.split(": ")[1]
            # สะสมบรรทัดของข้อมูลลงใน person_data
            person_data += line + '\n'

    # บันทึกข้อมูลของบุคคลสุดท้ายหากไม่มีบรรทัดว่างหลังข้อมูล
    if person_data:
        if person_type == "นักศึกษา":
            name = person_data.split('\n')[0]  # ชื่อจะเป็นบรรทัดแรก
            with open(student_file, 'a', encoding='utf-8') as f:
                f.write(f"{student_count}) {name}\n")
        elif person_type == "อาจารย์":
            name = person_data.split('\n')[0]  # ชื่อจะเป็นบรรทัดแรก
            with open(teacher_file, 'a', encoding='utf-8') as f:
                f.write(f"{teacher_count}) {name}\n")
            if faculty in faculty_dirs:
                faculty_file = os.path.join(faculty_dirs[faculty], f"รายชื่อคณาจารย์คณะ{faculty}.txt")
                with open(faculty_file, 'a', encoding='utf-8') as f:
                    f.write(f"{faculty_counts[faculty]}) {name}\n")

print("สร้างโครงสร้าง Directory และบันทึกข้อมูลเสร็จเรียบร้อย")
